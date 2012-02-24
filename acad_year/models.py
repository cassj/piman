from django.db import models

class AcademicYear(models.Model):
   term1_start = models.DateField()
   term1_end   = models.DateField(blank=True)
   term2_start = models.DateField(blank=True)
   term2_end   = models.DateField(blank=True)
   term3_start = models.DateField(blank=True) 
   term3_end   = models.DateField()
   notes       = models.TextField(blank=True)

   def __unicode__(self):
     return str(self.term1_start)


