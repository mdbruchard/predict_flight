from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('flights', views.get_flight, name='get_flight'),
    
    path('flight/<int:flight_id>', views.flight, name='flight')
]