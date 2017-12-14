from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.sign_up, name='sign_up'),
    url(r'^provider/dashboard/$', views.providerDashboard, name = 'providerDashboard'),
    url(r'^provider/prescriptions/$', views.providerPrescriptions, name = 'providerPrescriptions'),
    url(r'^patient/dashboard/$', views.patientDashboard, name = 'providerDashboard'),
    url(r'^patient/prescriptions/$', views.patientPrescriptions, name = 'providerPrescriptions'),
    url(r'^admin/stats/$', views.patientPrescriptions, name = 'adminStats'),
    url(r'^admin/landing/$', views.patientPrescriptions, name = 'adminLanding')
    # log in screen
    # sign up screen
    # dashboard for providers -> has a request Function
        # display prescriptions -> after a request, allow for a new script to be added
    # prescriptions page -> prescriptions a doctor has written

    # dashboard for patients -> has historical prescriptions displayed
]
