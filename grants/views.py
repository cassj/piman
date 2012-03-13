from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import *
from django.forms import ModelForm
from datetime import datetime
from students.models import *

# how to write a @is_manager decorator?
@login_required
def manage(request):

    try:
      manager = request.user.manager
      t = loader.get_template('grants/manager_manage.html')
      c = RequestContext(request, {})
      return HttpResponse(t.render(c))
    except:
      t = loader.get_template('pis/not_a_manager.html')
      c = RequestContext(request, {})
      return HttpResponse(t.render(c))

