from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from stormapp.deadbodies.models import DeadBody

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def report_dead_body(request):
    context = {}

    if request.method == 'POST':
        dead_body_form = DeadBodyForm(request.POST)
        if dead_body_form.is_valid():
            dead_body_form.save()
            context['dead_body_form'] = DeadBodyForm()
        else:
            context['dead_body_form'] = dead_body_form
    else:
        context['dead_body_form'] = DeadBodyForm()

    return render_to_response('deadbodies/' )

def view_all_dead_body(request):
    pass