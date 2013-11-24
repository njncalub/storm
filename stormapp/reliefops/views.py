from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from stormapp.reliefops.models import ReliefOps
from stormapp.reliefops.forms import RelOpsForm
from geopy import geocoders

def home_view(request):
    context = {}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
    #return HttpResponse("Hello, world. You're at the index.")

def sample_map_view(request):
    context = {}
    return render_to_response('sample_map.html', context, context_instance=RequestContext(request))

def report_relief_ops(request):
    context = {}

    if request.method == 'POST':
        relief_ops_form = RelOpsForm(request.POST, request.FILES)
        if relief_ops_form.is_valid():
            relief_ops = relief_ops_form.save(commit=False)
            nlat = 0.0
            nlong = 0.0

            location = relief_ops.location

            g = geocoders.GoogleV3()
            place, (lat, lng) = g.geocode(location)
            print "%s: %.5f, %.5f" % (place, lat, lng)

            relief_ops.nlat = lat
            relief_ops.nlong = lng

            relief_ops.save()
            
            context['relief_ops_form'] = RealOpsForm()
            print 'valid'
        else:
            print 'error'
            context['relief_ops_form'] = relief_ops_form
    else:
        context['relief_ops_form'] = RelOpsForm()

    return render_to_response('reliefops/report_relief_ops.html', context, context_instance=RequestContext(request) )


def view_all_relief_ops(request):
    context = {}

    rel_ops = ReliefOps.objects.all()

    context['rel_ops'] = rel_ops

    for d in rel_ops:
        print d.image

    return render_to_response('reliefops/view_all_relief_ops.html', context, context_instance=RequestContext(request) )


def retrieve_reliefops(request):
    context = {}

    pass


def center_finder(request):
    context = {}

    return render_to_response('reliefops/center_finder.html', context, context_instance=RequestContext(request) )