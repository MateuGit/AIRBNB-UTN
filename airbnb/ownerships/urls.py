from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('grid/', views.grid, name='grid'),
    path('reserve/', views.reserve, name='grid'),
    path('ownerships/', views.landing, name='ownerships'),
    path('ownerships/<int:ownership_id>/', views.detail, name='ownership-detail'),
]
