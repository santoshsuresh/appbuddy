from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from buddy.forms import AppBuddyPasswordResetForm
from buddy.views import DashboardView


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', DashboardView.as_view(), name='dashboard'),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^accounts/password_change/$', 'django.contrib.auth.views.password_change',
                           {'password_change_form': SetPasswordForm}, name='change_password'),
                       url(r'^accounts/password_reset/$', 'django.contrib.auth.views.password_reset',
                           {'password_reset_form': AppBuddyPasswordResetForm}, name='reset_password'),
                       url(r'^accounts/password_reset_done/$', 'django.contrib.auth.views.password_reset_done',
                           name='password_reset_done'),
                       url(r'^accounts/password_reset_complete/$', 'django.contrib.auth.views.password_reset_complete',
                           name='password_reset_complete'),
                       url(r'^accounts/password_reset_confirm/(?P<uidb64>.+)/(?P<token>.+)$', 'django.contrib.auth.views.password_reset_confirm',
                           name='password_reset_confirm'),
                       url(r'^accounts/password_change_done/$', 'django.contrib.auth.views.password_change_done',
                           name='password_change_done'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'},
                           name='logout', ),
                       url(r'^appbuddy/', include('buddy.urls')),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       # Examples:
                       # url(r'^$', 'appbuddy.views.home', name='home'),
                       # url(r'^appbuddy/', include('appbuddy.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       (r'^grappelli/', include('grappelli.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
    )
