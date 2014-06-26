from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import AppInfo
from .tasks import download_app_from_playstore


@receiver(post_save, sender=AppInfo)
def do_on_app_info_save(sender, instance, created, **kwargs):
    download_app_from_playstore.delay(app_id=instance.pk)

