from fabric.colors import red, green
from fabric.context_managers import cd, shell_env
from fabric.operations import run, sudo, local
from fabric.state import env

env.hosts = ["srv1.brandclub.mobi"]
env.user = 'bclub'

# To run use fab -H host_name -u user deploy_prod
#Host is srv1.brandclub.mobi user is bclub
def deploy():
    print(red("Deploying to production server"))
    local('git push origin master')
    with cd("/opt/bclub/appbuddy"):
        run("git reset --hard || true")
        run("git pull origin master")
        run("source /opt/bclub/.virtualenvs/buddyenv/bin/activate && pip install -r requirements.txt")
    with cd("/opt/bclub/appbuddy/appbuddy"):
        with shell_env(DJANGO_SETTINGS_MODULE='appbuddy.settings.production',
                       SECRET_KEY='bclubmfw0w!ipbgtlen=&m^3i(f$by2oi$$7!7$xrqioag3*^pane+0prod'):
            run(
                "source /opt/bclub/.virtualenvs/buddyenv/bin/activate && python manage.py collectstatic --noinput > /dev/null")
            run("source /opt/bclub/.virtualenvs/buddyenv/bin/activate && ./manage.py migrate --no-initial-data")
        sudo("supervisorctl restart appbuddy    ")
    print(green("Deployment complete"))
