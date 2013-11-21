from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'home.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'log/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'log/logged_out.html'}),
    url(r'^signup/$', 'log.views.signup', {'template_name': 'log/signup_form.html', 'email_template_name': 'log/signup_email.html'}),
    url(r'^signup/done/$', 'log.views.signup_done', {'template_name': 'log/signup_done.html'}),
    url(r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'log.views.signup_confirm'),
    url(r'^signup/complete/$', 'log.views.signup_complete', {'template_name': 'log/signup_complete.html'}),
    url(r'^user/profile/$', TemplateView.as_view(template_name='log/profile.html')),
    url(r'^accounts/', include('accounts.urls')),

    # Examples:
    # url(r'^$', 'hiplyst.views.home', name='home'),
    # url(r'^hiplyst/', include('hiplyst.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

