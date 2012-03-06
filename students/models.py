from django.db import models
from taggit.managers import TaggableManager

class StudyLevel(models.Model):
   name        = models.CharField(max_length=20)
   description = models.TextField(blank=True)

   def __unicode__(self):
      return self.name


class Student(models.Model):
   name        = models.CharField(max_length=100)
   description = models.TextField(blank=True)
   start_year  = models.ForeignKey('acad_year.AcademicYear', related_name="student_start_year")
   end_year    = models.ForeignKey('acad_year.AcademicYear', related_name="student_end_year")
   level       = models.ForeignKey(StudyLevel)

   def __unicode__(self):
      return self.name


class Project(models.Model):
   name         = models.CharField(max_length=255)
   description  = models.TextField(blank=True)
   supervisors  = models.ManyToManyField('pis.PI', through='ProjectPI', related_name='projects')
   start_year   = models.ForeignKey('acad_year.AcademicYear', related_name="project_start_year")
   end_year     = models.ForeignKey('acad_year.AcademicYear', related_name="project_end_year")
   students     = models.ManyToManyField(Student, blank=True, related_name="projects")
   notes        = models.TextField(blank=True)

   tags         = TaggableManager(blank=True)

   def __unicode__(self):
      return self.name

class Milestone(models.Model):
   project        = models.ForeignKey(Project)
   name           = models.CharField(max_length=100)
   description    = models.TextField()
   notes          = models.TextField(blank=True)
   due_date       = models.DateField()
   complete_date  = models.DateField(blank=True, null=True)

   tags           = TaggableManager(blank=True)

   def __unicode__(self):
      return self.name
   

class ProjectPI(models.Model):
   project     = models.ForeignKey(Project)
   pi          = models.ForeignKey('pis.PI')
   percentage  = models.IntegerField()
   notes       = models.TextField(blank=True)
   
   def __unicode__(self):
      return self.supervisor.user.name 


