from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addItem/', views.addItem, name='addItem'),
    path('delItem/<int:id>/', views.delItem, name='delItem'),
]
