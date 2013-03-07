from django.conf.urls import patterns, include, url
from compressor.signals import post_compress
from django.contrib import admin
from djangosuit.compress import post_less_compile

admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangosuit.views.home', name='home'),
    # url(r'^djangosuit/', include('djangosuit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# Post compress handler for less files
post_compress.connect(post_less_compile)
