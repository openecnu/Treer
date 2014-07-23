from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()
handler404 = 'treer.views.error_404'
handler500 = 'treer.views.error_500'
urlpatterns = patterns('',
    url(r'^$','treer.views.index'),
    url(r'^log/','treer.views.log'),
    url(r'^contact/','treer.views.contact'),
    url(r'^thanks/','treer.views.thanks'),
    # Examples:
    # url(r'^$', 'treer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
)
