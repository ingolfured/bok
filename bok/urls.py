from django.conf.urls import include, patterns, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^leita/$', 'baekur.views.leita'),
    url(r'^selja/$', 'baekur.views.selja'),
)

