from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import *
from pis.models import Manager,PI
from datetime import datetime
from django import forms
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):

   pi = request.user.pi
   # Have to use RequestContext rather than just Context to get
   # STATIC_URL working. As we're using this to serve css and js files,
   # we need to use it for all views.
   #pi = get_object_or_404(PI, pk=pi_id)
   projects = pi.projects.all()

   teaching_commitments = pi.teaching_commitments.all()   

   applications = pi.applications.all()
   submitted_applications = applications.filter(submitted_grant__decision_date__gte=datetime.now())
   awarded_applications = applications.filter(submitted_grant__award__isnull=False)
  
   try:
     publications = pi.author.publications.all()
   except ObjectDoesNotExist:
     publications = []


   t = loader.get_template('pis/pi_home.html')
   c = RequestContext(request, {'pi'                     : pi,
                                'projects'               : projects,
                                'teaching_commitments'   : teaching_commitments,
                                'submitted_applications' : submitted_applications,
                                'awarded_applications'   : awarded_applications,
                                'publications'           : publications })

   return HttpResponse(t.render(c))


@login_required
def manager_home(request, manager_id):

   manager = get_object_or_404(Manager, pk=manager_id)
   t = loader.get_template('pis/manager_home.html')
   c = RequestContext(request, {'manager': manager})
   return HttpResponse(t.render(c))

