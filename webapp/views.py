from django.http import HttpResponse


def login(request):
    return HttpResponse("Login to Optrak")


def sign_up(request):
    return HttpResponse("Sign up for Optrak")
