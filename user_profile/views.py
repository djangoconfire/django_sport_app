from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from user_profile.models import *
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from user_profile.models import UserProfile
from user_profile.forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'signup.html', {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            djangouser = User(username=username)
            djangouser.set_password(password)
            djangouser.email = email
            try:
                djangouser.save()
            except Exception as e:
                form = SignUpForm()
                return render(request, 'signup.html', {'form': form})

            new_user = UserProfile()

            user = authenticate(username=username, password=password)
            ## user has been added to the current session
            new_user.user = djangouser
            new_user.save()

            login(request, user)

            return redirect('/accounts/login/')
    else:
        return render(request, 'signup.html', {'form': SignUpForm()})


def user_login(request):
    context = RequestContext(request)
    if request.user.is_authenticated():
        # check if a user is authenticate
        try:
            # try if userprofile exists
            user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            # if userprofile doesnot exist, redirect to all contests page
            return HttpResponseRedirect("/")
    if request.method == "GET":
        # if next is there in request.GET, send next in request data
        if 'next' in request.GET:
            next_page = request.GET['next']
        else:
            next_page = ""
        return render_to_response('login.html', {"next": next_page}, context_instance=RequestContext(request))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            user = UserProfile.objects.get(user=user)
            return HttpResponseRedirect('/' + 'user/' + request.POST.get('username', ''))

        else:
            return render(request,"login.html", {"next": request.POST['next'],
                                                     "error": "Invalid username or password."})



@login_required
def user_logout(request):
    try:
        logout(request)
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect("/")



@login_required
def user_profile(request, username):
    if request.user.is_authenticated():
        try:
            user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            message = "UserProfile does not exist"
            return render_to_response('500.html', {'error': message}, context_instance=RequestContext(request))
    return render_to_response('dashboard.html',{},context_instance=RequestContext(request))






