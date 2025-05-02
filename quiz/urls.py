# quiz/urls.py

from django.urls import path
from . import views
from .views import create_admin

urlpatterns = [
    path('', views.home, name='home'),
    path('tests/<str:level>/<str:category>/', views.test_list, name='test_list'),
    path('test/<int:test_id>/', views.take_test, name='take_test'),
    path('create-admin/', create_admin, name='create_admin'),
]
