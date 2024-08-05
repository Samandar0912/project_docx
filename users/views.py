from django.shortcuts import render, redirect
from .forms import SignupForm, UpdateProfileForm
from django.views import View
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import CustomUser

# Create your views here.


class SignupView(UserPassesTestMixin ,View):
    def get(self,request):
        return render(request,'registration/signup.html',{'form':SignupForm()})
    
    def post(self,request):
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Yangi profil yaratildi')
            return redirect('login')
        return render(request,'registration/signup.html',{'form':form})
            
    def test_func(self):
        user = self.request.user 
        if user.is_authenticated:
            return False
        return True
            

class ProfileView(View):
    def get(self,request, username):
        user = get_object_or_404(CustomUser,username=username)
        return render(request, 'profile.html',{'customuser':user})
    
    
class UpdateProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    
    def get(self,request):
        form = UpdateProfileForm(instance=request.user)
        return render(request,'profile_update.html', {'form':form})
    
    def post(self,request):
        form = UpdateProfileForm( instance=request.user ,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Profil Taxrirlandi')
            return redirect('users:profile', request.user)
        return render(request,'registration/signup.html',{'form':form})