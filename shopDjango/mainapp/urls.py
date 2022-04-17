from django.urls import path
from . import views

app_name = 'mainapp'

# urlpatterns = [
#     # post views
#     path('login/', views.user_login, name='login'),
#

from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('login/', LoginView.as_view(template_name="mainapp/login.html"), name='login'),
]
