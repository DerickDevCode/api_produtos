from django.urls import path

from api.base.views import home

urlpatterns = [
    path('', home, name='home'),
]
