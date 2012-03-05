from django.db import models
from taggit.managers import TaggableManager



class Module(models.Model):
   name         = models.CharField(max_length=100)
   description  = models.TextField(blank=True)
   notes        = models.TextField(blank=True)
   code         = models.CharField(max_length=30)

   tags         = TaggableManager()

   def __unicode__(self):
      return self.name

class Course(models.Model):
   name         = models.CharField(max_length=100)
   description  = models.TextField(blank=True)
   notes        = models.TextField(blank=True)
   years        = models.ManyToManyField('acad_year.AcademicYear', through='CourseYear', related_name='course')
   modules      = models.ManyToManyField(Module, through='CourseModule', related_name='courses')

   tags         = TaggableManager()

   def __unicode__(self):
      return self.name

class CourseYear(models.Model):
   course       = models.ForeignKey(Course)
   year         = models.ForeignKey('acad_year.AcademicYear')
   organisers    = models.ManyToManyField('pis.PI', related_name='organised_courses')


class CourseModule(models.Model):
    module              = models.ForeignKey(Module)
    course              = models.ForeignKey(Course)
    year                = models.ForeignKey('acad_year.AcademicYear')
    start_date          = models.DateField()
    end_date            = models.DateField()
    organisers          = models.ManyToManyField('pis.PI', related_name='organised_modules')
    teachers            = models.ManyToManyField('pis.PI', through='TeachingCommitment')


class TeachingCommitment(models.Model):
   course_module = models.ForeignKey(CourseModule)
   pi            = models.ForeignKey('pis.PI', related_name='teaching_commitments')
   contact_hours = models.DecimalField(max_digits=5, decimal_places=2)
   notes         = models.TextField(blank=True)


