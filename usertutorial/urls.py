from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'usertutorial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^signup/$', 'security.views.signup', name='signup'),

    url(r'^secret/$', 'security.views.special_page', name='special'),

    url(r'^accounts/login/$', 'security.views.login_view', name='login'),





)

