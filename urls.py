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

    url(r'^accounts/login','django.contrib.auth.views.login'),
    url(r'^accounts/logout','django.contrib.auth.views.logout'),
    url(r'^accounts/register','pis.views.register'), 
    url(r'^accounts/profile','pis.views.profile'),
    url(r'^pis/students_block', 'pis.views.students_block'),
    url(r'^pis/teaching_block', 'pis.views.teaching_block'),
    url(r'^pis/grants_block', 'pis.views.grants_block'),
    url(r'^pis/publications_block', 'pis.views.publications_block'),

    url(r'grants', 'grants.views.manage'),
    url(r'publications','publications.views.manage'),
    url(r'students', 'students.views.manage'),
    url(r'courses', 'courses.views.manage'),
    url(r'projects', 'projects.views.manage'),


    # CRUD 
    # Student projects 
    url(r'^student/create', 'students.views.student_create'),
    url(r'^study_level/create', 'students.views.study_level_create'),
    url(r'^project/create', 'students.views.project_create'),
    url(r'^project_pi/create', 'students.views.project_pi_create'),
    url(r'^milestone/create', 'students.views.milestone_create'),

    url(r'^student/(?P<student_id>\d+)/edit$', 'students.views.student_edit'),
    url(r'^study_level/(?P<study_level_id>\d+)/edit$', 'students.views.study_level_edit'),
    url(r'^project/(?P<project_id>\d+)/edit$', 'students.views.project_edit'),
    url(r'^project_pi/(?P<project_pi_id>\d+)/edit$', 'students.views.project_pi_edit'),
    url(r'^milestone/(?P<milestone_id>\d+)/edit$', 'students.views.milestone_edit'),
 

)
