from django.shortcuts import render
from .models import *

def home(request):
    topics = Topics.objects.all()
    context = {"topics":topics}
    return render(request, "base/home.html", context)

def register(request):
    return render(request, 'user/register.html',)
