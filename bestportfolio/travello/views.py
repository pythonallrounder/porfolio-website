from django.shortcuts import render
from travello.models import *
# Create your views here.


def index2(request):
    return render(request,'index1.html')
