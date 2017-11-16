from django.http import HttpResponse

def login(request):
    return HttpResponse("Login to Optrak")

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
