from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('propiedades/', views.grid, name='ownerships'),
    path('propiedades/<int:ownership_id>/', views.reserve, name='reserve'),
]
