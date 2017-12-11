from django.shortcuts import render

from webapp.forms import UserForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
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
	            return HttpResponseRedirect(reverse('index'))
	        else:
	            # If account is not active:
	            return HttpResponse("Your account is not active.")
	    else:
	        print("Someone tried to login and failed.")
	        print("They used username: {} and password: {}".format(username,password))
	        return HttpResponse("Invalid login details supplied.")

    else:
    	return render(request, "index.html")

def sign_up(request):
    # store their public key on the blockchain
    return HttpResponse("Sign up for Optrak")

def providerDashboard(request):
    return HttpResponse("Provider Dashboard")

def patientDashboard(request):
    return HttpResponse("Patient Dashboard")

def patientPrescriptions(request):
    return HttpResponse("Patient Prescriptions")

def providerPrescriptions(request):
    return HttpResponse("Provider Prescriptions")
