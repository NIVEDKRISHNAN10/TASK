from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from bankapp.forms import UserForm
# Create your views here.
def home(request):
    return render(request,'home.html')
def redirect_to_wikipedia(request, district):

    return redirect('https://en.wikipedia.org/wiki/' + district)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return HttpResponseRedirect('/register/')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return HttpResponseRedirect('/user_login/')
        else:
            messages.info(request, "Passwords do not match")
            return HttpResponseRedirect('/register/')

    return render(request, "register.html")



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/page/')
        else:
            messages.info(request, 'invalid')
            return HttpResponseRedirect('/user_login/')
    return render(request, "login.html")
def page(request):
    return render(request,'page.html')

def form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Application accepted"
            return HttpResponseRedirect('/process_form/')
    else:
        form = UserForm()
        form.fields['branch'].choices = form.get_branch_choices(form.initial.get('district'))

    return render(request, 'form.html', {'form': form})





def success_page(request):
    message = "Application accepted"
    return render(request, 'success_page.html', {'message': message})

def user_logout(request):
    auth.logout(request)
    return redirect('/')