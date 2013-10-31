from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^login/$', 'log.views.login'),
    url(r'^logout/$', 'log.views.logout'),
    url(r'^signup/$', 'log.views.signup'),
    # Examples:
    # url(r'^$', 'hiplyst.views.home', name='home'),
    # url(r'^hiplyst/', include('hiplyst.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
