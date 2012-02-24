from django.db import models
from taggit.managers import TaggableManager

class AwardingBody(models.Model):
   name        = models.CharField(max_length=100)
   description = models.TextField(blank=True)

   tags         = TaggableManager()

   def __unicode__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Awarding Bodies"


class Grant(models.Model):  
   title         = models.TextField()
   description   = models.TextField(blank=True)
   awarding_body = models.ForeignKey(AwardingBody)

   tags         = TaggableManager()

   def __unicode__(self):
      return self.title


# remodel this as manytomany wth submitted grant and user with intermediate table,
#class Applicant(models.Model):
#   user             = models.ForeignKey('auth.User')
#   grant            = models.ForeignKey(SubmittedGrant)
#   percentage_split = models.DecimalField(max_digits=5,decimal_places=2)
#
#   def __unicode__(self):
#      return self.question
#

class SubmittedGrant(models.Model):
   grant                = models.ForeignKey(Grant)
   title                = models.TextField()
   abstract             = models.TextField()
   decision_date        = models.DateField()
   estimated_start_date = models.DateField()
   estimated_end_date   = models.DateField()
   total_value          = models.DecimalField(max_digits=10, decimal_places=2)
   fEC                  = models.DecimalField("Full Economic Cost", max_digits=10, decimal_places=2)
#   applications         = models.ManyToManyField(Applicant)
   
   def __unicode__(self):
      return self.grant.title

# remodel this as manytomany wth submitted grant and user with intermediate table,
class Applicant(models.Model):
   user             = models.ForeignKey('auth.User')
   grant            = models.ForeignKey(SubmittedGrant)
   percentage_split = models.DecimalField(max_digits=5,decimal_places=2)

   def __unicode__(self):
      return self.question




class AwardedGrant(models.Model):
   submission    = models.ForeignKey(SubmittedGrant)
   start_date     = models.DateField()
   end_date       = models.DateField()

   def __unicode__(self):
      return self.question


# maybe need to add more stuff for tracking awarded grants, cost codes, spending etc?


