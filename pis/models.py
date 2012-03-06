from django.db import models

# This is just an extension of the built-in django groups
# to add extra information fields. 
class GroupInfo(models.Model):
   group       = models.ForeignKey('auth.Group')
   description = models.TextField(blank = True)

   def __unicode__(self):
      return self.name

TITLE_CHOICES = (
   ('MR', 'Mr'),
   ('MISS', 'Miss'),
   ('MS', 'Ms'),
   ('MRS', 'Mrs'),
   ('DR', 'Doctor'),
   ('PROF', 'Professor')
)

class Rank(models.Model):
  name  = models.CharField(max_length=100)
  description = models.TextField(blank=True)

  def __unicode__(self):
    return self.name

class PI(models.Model):
   user        = models.OneToOneField('auth.User', related_name="pi")
   title       = models.CharField(max_length=4, choices=TITLE_CHOICES)
   rank        = models.ForeignKey(Rank)
   telephone   = models.CharField(max_length=30)

   def __unicode__(self):
      return self.user.username


class Manager(models.Model):
    user       = models.OneToOneField('auth.User', related_name="manager")

    def __unicode__(self):
      return self.user.username



