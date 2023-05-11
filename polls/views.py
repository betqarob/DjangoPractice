from django.shortcuts import render
from django.http import HttpResponse

# just testing to make sure that views file works as intended (ft. html code :D)
def index(request):
    return HttpResponse("<h1> Hello Richard</h1>")