from django.db import models
from taggit.managers import TaggableManager


class Journal(models.Model):
   title       = models.CharField(max_length=255)
   description = models.TextField()

   tags         = TaggableManager()

   def __unicode__(self):
      return self.title


class Paper(models.Model):
   title               = models.TextField()
   abstract            = models.TextField()
   journal_title       = models.ForeignKey(Journal)
   publication_date    = models.DateField()
   number_of_citations = models.IntegerField()
   doi                 = models.CharField(max_length=50)

   tags                = TaggableManager()

   def __unicode__(self):
      return self.title
