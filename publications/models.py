from django.db import models
from taggit.managers import TaggableManager


class Journal(models.Model):
   title       = models.CharField(max_length=255)
   description = models.TextField()

   tags         = TaggableManager()

   def __unicode__(self):
      return self.title


class Author(models.Model):
    initials           = models.CharField(max_length=5)
    surname            = models.CharField(max_length=255)
    pi                 = models.OneToOneField('pis.PI', null=True, related_name='author')  
 
    def __unicode__(self):
        return self.initials + ' ' + self.surname  

class Paper(models.Model):
   title               = models.TextField()
   abstract            = models.TextField()
   journal             = models.ForeignKey(Journal)
   publication_date    = models.DateField()
   number_of_citations = models.IntegerField()
   doi                 = models.CharField(max_length=50)
   authors             = models.ManyToManyField(Author, through='Publication', related_name='papers')

   tags                = TaggableManager()

   def __unicode__(self):
      return self.title

class Publication(models.Model):
    author = models.ForeignKey(Author, related_name='publications')
    paper  = models.ForeignKey(Paper)
    rank   = models.IntegerField()


