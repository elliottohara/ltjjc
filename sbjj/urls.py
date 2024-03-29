from django.conf.urls import patterns, include, url

from django.contrib import admin
import website

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sbjj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'website.views.index', name='home'),
    url(r'^about$', 'website.views.about', name='about'),
    url(r'^t$', 'website.views.test', name='test'),
    url(r'^classes$', 'website.views.classes', name='classes'),
    url(r'^staff$', 'website.views.staff', name="staff"),
    url(r'^staff/(?P<staff_name>\w+)/$', 'website.views.staffdetail', name='staff_detail'),
    url(r'^sql$','website.views.sql'),
    url(r'^children$', 'website.views.children', name='children')

)
