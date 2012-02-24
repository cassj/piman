from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, get_object_or_404
from pis.models import Manager,PI


def pi_home(request, pi_id):

   # Have to use RequestContext rather than just Context to get
   # STATIC_URL working. As we're using this to serve css and js files,
   # we need to use it for all views.
   pi = get_object_or_404(PI, pk=pi_id)
   t = loader.get_template('pis/pi_home.html')
   c = RequestContext(request, {'pi': pi})
   return HttpResponse(t.render(c))


def manager_home(request, manager_id):

   manager = get_object_or_404(Manager, pk=manager_id)
   t = loader.get_template('pis/manager_home.html')
   c = RequestContext(request, {'manager': manager})
   return HttpResponse(t.render(c))

