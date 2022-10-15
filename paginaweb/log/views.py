from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegistrateForm
from django.contrib import messages
# Create your views here.


def home (request):
    return render(request,'paginas/index.html')



def registro (request):
    if request.method == "POST":
        form = UserRegistrateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hola {username}, your account was created successfully')
            return redirect( 'home')
    else:
        form = UserRegistrateForm()

    return render(request, 'paginas/registro.html', {'form': form})


def profile (request):
    return render(request,'paginas/profile.html')
