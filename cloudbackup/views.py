from django.shortcuts import render
from django.http  import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    return render(request,'cloudUps/homepage.html')
    
@login_required(login_url='/login/')
def index(request):


    return redirect(request,'index.html')