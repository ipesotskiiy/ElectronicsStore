from django.urls import path
from django.views.generic import TemplateView
from mainapp.views import *

app_name = 'user'

urlpatterns = [
    path('invalid_verify/', TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),
    path('registration/', Registration.as_view(), name='registration'),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('profile/', ProfileView.as_view(), name='profile_page')
]
