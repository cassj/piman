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


def get_projects(pi):
  try:
    projects = pi.projects.all()
  except ObjectDoesNotExist:
    projects = []
  return projects

def get_teaching_commitments(pi):
  try:
    teach = pi.teaching_commitments.all()
  except ObjectDoesNotExist:
    teach = []
  return teach  

def get_applications(pi):
  try:
    applications =  pi.applications.all()
  except ObjectDoesNotExist:
    return [],[]

  submitted_applications = applications.filter(submitted_grant__decision_date__gte=datetime.now())
  awarded_applications = applications.filter(submitted_grant__award__isnull=False)
  return submitted_applications, awarded_applications

def get_publications(pi):
  try:
    publications = pi.author.publications.all()
  except ObjectDoesNotExist:
    publications = []
  return publications

@ajax_login_required
def students_block(request):
  try:
    pi = request.user.pi
    projects = get_projects(pi)
    t = loader.get_template('pis/students.html')
    c = RequestContext(request, {'pi'       : pi,
                                 'projects' : projects }  )
    html = t.render(c)
  except ObjectDoesNotExist:
    # this should fire a js warning that user is not a PI
    html = ""
  
  response =  HttpResponse(json.dumps({'html' : html}), mimetype=u'application/json')
  return response

@ajax_login_required
def teaching_block(request):
  try:
    pi = request.user.pi
    teaching_commitments = get_teaching_commitments(pi)
    t = loader.get_template('pis/teaching.html')
    c = RequestContext(request, {'pi'       : pi,
                                 'teaching_commitments' : teaching_commitments }  )
    html = t.render(c)
  except ObjectDoesNotExist:
    html = ""

  response = HttpResponse(json.dumps({'html' : html}), mimetype=u'application/json')
  return response

@ajax_login_required
def grants_block(request):
  try:
    pi = request.user.pi
    submitted_applications, awarded_applications = get_applications(pi)
    t = loader.get_template('pis/grants.html')
    c = RequestContext(request, {'pi'                      : pi,
                                 'submitted_applications'  : submitted_applications,
                                 'awarded_applications'    : awarded_applications })    
    html = t.render(c)
  except ObjectDoesNotExist:
    html =  ""

  response = HttpResponse(json.dumps({'html' : html}), mimetype=u'application/json')
  return response


@ajax_login_required
def publications_block(request):
  try: 
    pi = request.user.pi
    publications = get_publications(pi)
    t = loader.get_template('pis/publications.html')
    c = RequestContext(request, {'pi'           : pi, 
                                 'publications' : publications })
    html = t.render(c)
  except ObjectDoesNotExist:
    html = ""

  response = HttpResponse(json.dumps({'html' : html}), mimetype=u'application/json')
  return response


@login_required
def profile(request):

  try:
    pi = request.user.pi
    projects = get_projects(pi)
    teaching_commitments = get_teaching_commitments(pi)
    submitted_applications, awarded_applications = get_applications(pi)
    publications = get_publications(pi)

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



def register(request):

  t = loader.get_template('registration/registration_form.html')
  c = RequestContext(request,{})
  html = t.render(c)
  response =  HttpResponse(json.dumps({'html' : html}), mimetype=u'application/json')
  return(response)



