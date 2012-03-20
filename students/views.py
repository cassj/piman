from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import *
from django.forms import ModelForm
from datetime import datetime
from students.models import *
from functions import *
import json

class StudyLevelForm(ModelForm):
  class Meta:
    model = StudyLevel

def study_level_create(request):
  if request.method == 'POST':
    form = StudyLevelForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/study_level/create')
  else:
    form = StudyLevelForm()
  
  t = loader.get_template('students/study_level_create.html')
  c = RequestContext(request, {'form' : form } )
  return HttpResponse(t.render(c))

def study_level_edit(request, study_level_id):
  if request.method == 'POST':
    form = StudyLevelForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/study_level/edit')
  else:
    study_level = get_object_or_404(StudyLevel, pk=study_level_id)
    form = StudyLevelForm(instance=study_level)

  t = loader.get_template('students/study_level_edit.html')
  c = RequestContext(request, {'form' : form, 'id' : study_level.id } )
  return HttpResponse(t.render(c))


class StudentForm(ModelForm):
  class Meta:
    model = Student

def student_create(request):
  if request.method == 'POST': 
    form = StudentForm(request.POST) 
    if form.is_valid(): 
      form.save()
      return HttpResponseRedirect('/student/create') 
  else:
    form = StudentForm() 

  t = loader.get_template('students/student_create.html')
  c = RequestContext(request, {'form' : form } )
  return HttpResponse(t.render(c))

def student_edit(request, student_id):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('students/student_edit.html')
  else:
    student = get_object_or_404(Student, pk=student_id)
    form = StudentForm(instance=student)

  t = loader.get_template('students/student_edit.html')
  c = RequestContext(request, {'form' : form, 'id' : student.id } )
  return HttpResponse(t.render(c))



class ProjectForm(ModelForm):
  class Meta:
    model = Project

def project_create(request):
  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/project/create')
  else:
    form = ProjectForm()

  t = loader.get_template('students/project_create.html')
  c = RequestContext(request, { 'form'  : form,
                                 'user' : request.user } )
  return HttpResponse(t.render(c))

@ajax_login_required
def project_edit(request, project_id):

  if request.method == 'POST':
    form = ProjectForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('students/project_edit.html')
  else:
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(instance=project)

  t = loader.get_template('students/project_edit.html')
  c = RequestContext(request, {'form' : form, 'id' : project.id } )
  html = t.render(c)
 
  # return the html as a json object in data.html
  # possibly for debugging this should just return the html if a get req.
  response =  HttpResponse(json.dumps({'html' : html}), mimetype=u'application/json')
  return response
  


class MilestoneForm(ModelForm):
  class Meta:
    model = Milestone

def milestone_create(request):
  if request.method == 'POST':
    form = MilestoneForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/milestone/create')
  else:
    form = MilestoneForm()

  t = loader.get_template('students/milestone_create.html')
  c = RequestContext(request, {'form' : form } )
  return HttpResponse(t.render(c))

def milestone_edit(request, milestone_id):
  if request.method == 'POST':
    form = MilestoneForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('students/milestone_edit.html')
  else:
    milestone = get_object_or_404(Milestone, pk=milestone_id)
    form = MilestoneForm(instance=milestone)

  t = loader.get_template('students/milestone_edit.html')
  c = RequestContext(request, {'form' : form, 'id': milestone.id } )
  return HttpResponse(t.render(c))




class ProjectPIForm(ModelForm):
  class Meta:
    model = ProjectPI


def project_pi_create(request):
  if request.method == 'POST':
    form = ProjectPIForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/project_pi/create')
  else:
    form = ProjectPIForm()

  t = loader.get_template('students/project_pi_create.html')
  c = RequestContext(request, {'form' : form } )
  return HttpResponse(t.render(c))


def project_pi_edit(request, project_pi_id):
  if request.method == 'POST':
    form = ProjectPIForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('students/project_pi_edit.html')
  else:
    project_pi = get_object_or_404(ProjectPI, pk=project_pi_id)
    form = ProjectPIForm(instance=project_pi)

  t = loader.get_template('students/project_pi_edit.html')
  c = RequestContext(request, {'form' : form, 'id' : project_pi.id} )
  return HttpResponse(t.render(c))




