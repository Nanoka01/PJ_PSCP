from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("ratanakron")

def about(request):
    return HttpResponse("<h1>เกี่ยวกับเรา</h1>")

def form(request):
    return HttpResponse("<h1>ฟรอมdata</h1>")
