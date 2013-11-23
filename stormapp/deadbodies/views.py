from deadbodies.models import DeadBody
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def report_dead_body(request):
    pass

def view_all_dead_body(request):
    pass