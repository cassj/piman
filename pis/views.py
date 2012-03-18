from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import *
from pis.models import Manager,PI
from datetime import datetime
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from functions import ajax_login_required
import models
import json
import re

#def ajax_login_request(request):
#
#  # this is useful for debugging - you can GET the page 
#  # directly so you see any error messages.
#  # don't use in production though.
#  try:
#    request.POST[u'login']
#    dictionary = request.POST
#  except:
#    dictionary = request
#
#  user = authenticate(username = dictionary[u'login'],
#                      password = dictionary[u'password'])
#
#  if user and user.is_active:
#    login(requst,user)
#    result = True
#  else:
#    result = False
#
#  response = HttpResponse(json.dumps(result), mimetype=u'application/json')
#  return response


@login_required
def profile(request):

  try:
    pi = request.user.pi
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
  except ObjectDoesNotExist:
    try:
      manager = request.user.manager

      t = loader.get_template('pis/manager_home.html')
      c = RequestContext(request,{'manager'                : manager})
      return HttpResponse(t.render(c))

    except ObjectDoesNotExist:
      # This should probably raise an exception.
      t = loader.get_template('pis/user_not_found.html')
      c = RequestContext(request, {})
      return HttpResponse(t.render(c))
      


@login_required
def manager_home(request, manager_id):

   manager = get_object_or_404(Manager, pk=manager_id)
   t = loader.get_template('pis/manager_home.html')
   c = RequestContext(request, {'manager': manager})
   return HttpResponse(t.render(c))

