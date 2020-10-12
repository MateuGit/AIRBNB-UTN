from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ownerships/', views.home, name='ownerships'),
    path('ownerships/<int:ownership_id>/', views.detail, name='ownership-detail'),
]
