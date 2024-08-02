from django.shortcuts import render
from .forms import SignupForm
from django.views import View

# Create your views here.


class SignupView(View):
    def get(self,request):
        return render(request,'registration/signup.html',{'form':SignupForm()})