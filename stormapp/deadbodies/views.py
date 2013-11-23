from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from stormapp.deadbodies.models import DeadBody
from stormapp.deadbodies.forms import DeadBodyForm

def home_view(request):
    context = {}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
    #return HttpResponse("Hello, world. You're at the index.")

def sample_map_view(request):
    context = {}
    return render_to_response('sample_map.html', context, context_instance=RequestContext(request))

def report_dead_body(request):
    context = {}

    if request.method == 'POST':
        dead_body_form = DeadBodyForm(request.POST, request.FILES)
        if dead_body_form.is_valid():
            dead_body_form.save()
            context['dead_body_form'] = DeadBodyForm()
            print 'valid'
        else:
            print 'error'
            context['dead_body_form'] = dead_body_form
    else:
        context['dead_body_form'] = DeadBodyForm()

    return render_to_response('deadbodies/report_dead_body.html', context, context_instance=RequestContext(request) )

def view_all_dead_body(request):
    pass