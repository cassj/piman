from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'piman.views.home', name='home'),
    # url(r'^piman/', include('piman.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

     url(r'^pi/(?P<pi_id>\d+)/$', 'pis.views.pi_home'),
     url(r'manager/(?P<manager_id>\d+)$','pis.views.manager_home')

#    url(r'^pi/(?P<pi_id>\d+)/grants/?$', 'grants.views.grants_by_piid')
#    url(r'^pi/(?P<pi_id>\d+)/publication/?$', 'publications.views.pubs_by_piid')
#    url(r'^pi/(?P<pi_id>\d+)/students/?$', 'students.views.students_by_piid')
#    url(r'^pi/(?P<pi_id>\d+)/courses/?$', 'courses.views.teaching_by_piid')
#    url(r'^pi/(?P<pi_id>\d+)/projects/?$', 'projects.views.projects_by_piid')



)
