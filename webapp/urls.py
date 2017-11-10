from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^$signup/', views.sign_up, name='sign_up'),
    url(r'^$provider/dashboard/', views.providerDashboard, name = 'providerDashboard'),
    url(r'^$provider/prescriptions/', views.providerPrescriptions, name = 'providerPrescriptions'),
    url(r'^$patient/dashboard/', views.patientDashboard, name = 'patientDashboard'),
    url(r'^$patient/prescriptions/', views.patientPrescriptions, name = 'patientPrescriptions'),
    # log in screen
    # sign up screen
    # dashboard for providers -> has a request Function
        # display prescriptions -> after a request, allow for a new script to be added
    # prescriptions page -> prescriptions a doctor has written

    # dashboard for patients -> has historical prescriptions displayed
]
