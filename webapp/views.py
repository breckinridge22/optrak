from django.shortcuts import render, redirect

from webapp.forms import UserForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms


def index(request):
    if request.method == 'POST':
    	if 'login' in request.POST:
    		return handleLogin(request)
    	elif 'register' in request.POST:
    		return handleRegister(request)
    else:
    	return render(request, 'index.html', {})

def handleLogin(request):
    # First get the username and password supplied
    username = request.POST.get('username')
    password = request.POST.get('password')

    # Django's built-in authentication function:
    user = authenticate(username=username, password=password)

    # If we have a user
    if user:
        #Check it the account is active
        if user.is_active:
            # Log the user in.
            login(request,user)
            # Send the user back to some page.
            # In this case their homepage.
            return HttpResponseRedirect(reverse('webapp:providerDashboard'))
        else:
            # If account is not active:
            return HttpResponse('Your account is not active.')
    else:
        print('Someone tried to login and failed.')
        print('They used username: {} and password: {}'.format(username,password))
        return HttpResponse('Invalid login details supplied.')

def handleRegister(request):
    registered = False

    # Get info from 'both' forms
    # It appears as one form to the user on the .html page
    user_form = UserForm(data=request.POST)

    # Check to see both forms are valid
    if user_form.is_valid():

        # Save User Form to Database
        user = user_form.cleaned_data
        username = user['username']
        password = user['password']
        email = user['email']

        # check if password is hashed
        if not(User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists()):
            
            User.objects.create_user(username, email, password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('webapp:providerDashboard'))
        else:
            raise forms.ValidationError()


        # Hash the password
        # user.set_password(user.password)

        # Update with Hashed password
        # user.save()
        # print('----------------------------------------registering-----------' + user.password)

        # Registration Successful!
        registered = True
        # return render(request, 'index.html', {'user_form': user_form, 'registered': registered})

    else:
        # One of the forms was invalid if this else gets called.
        user_form = UserForm()
        
    print(user_form.errors)
    return render(request, 'error.html', {'form': user_form})



def sign_up(request):
    # store their public key on the blockchain
    return HttpResponse('Sign up for Optrak')

def providerDashboard(request):
    return HttpResponse('Provider Dashboard')

def patientDashboard(request):
    return HttpResponse('Patient Dashboard')

def patientPrescriptions(request):
    return HttpResponse('Patient Prescriptions')

def providerPrescriptions(request):
    return HttpResponse('Provider Prescriptions')
