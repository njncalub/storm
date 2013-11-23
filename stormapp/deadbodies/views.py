from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from stormapp.deadbodies.models import DeadBody
from stormapp.deadbodies.forms import DeadBodyForm
from geopy import geocoders

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
            dead_body = dead_body_form.save(commit=False)
            nlat = 0.0
            nlong = 0.0

            location = dead_body.location

            g = geocoders.GoogleV3()
            place, (lat, lng) = g.geocode(location)
            print "%s: %.5f, %.5f" % (place, lat, lng)

            dead_body.nlat = lat
            dead_body.nlong = lng

            dead_body.save()
            
            context['dead_body_form'] = DeadBodyForm()
            print 'valid'
        else:
            print 'error'
            context['dead_body_form'] = dead_body_form
    else:
        context['dead_body_form'] = DeadBodyForm()

    return render_to_response('deadbodies/report_dead_body.html', context, context_instance=RequestContext(request) )

def view_all_dead_body(request):
    context = {}

    dead_bodies = DeadBody.objects.all()

    context['dead_bodies'] = dead_bodies

    for d in dead_bodies:
        print d.image

    return render_to_response('deadbodies/view_all_dead_bodies.html', context, context_instance=RequestContext(request) )