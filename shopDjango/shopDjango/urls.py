"""shopDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import BaseView
from shopDjango.swagger import schema

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('user/', include('mainapp.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('product/', include('product.urls')),
    path('orders/', include('order.urls')),
]


def get_swagger(request):
    return JsonResponse(schema.to_dict(), json_dumps_params={'indent': 2})


urlpatterns += [
    path('swagger/', get_swagger),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
