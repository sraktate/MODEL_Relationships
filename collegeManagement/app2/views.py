from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


# Create your views here.

def UserRegisterView(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name = 'app2/userRegister.html'
    context = {'form': form}
    return render(request, template_name, context)



def loginView(request):
    if request.method == 'POST':
        U = request.POST.get('un')
        P = request.POST.get('Pass')
        User = authenticate(username=U,password=P)

        if User is not None:
            login(request,User)
            return redirect('Home')
        else:
            messages.error(request,'Invalid Credentials')
    template_name = 'app2/login.html'
    context = {}
    return render(request,template_name,context)

def logoutView(request):
    logout(request)
    return redirect('login')