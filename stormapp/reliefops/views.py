from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from stormapp.deadbodies.models import DeadBody
from stormapp.deadbodies.forms import DeadBodyForm
from geopy import geocoders

def center_finder(request):
    context = {}

    return render_to_response('reliefops/center_finder.html', context, context_instance=RequestContext(request) )
