from django.urls import path

from home.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
]
