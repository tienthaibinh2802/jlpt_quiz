# quiz/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tests/<str:level>/<str:category>/', views.test_list, name='test_list'),
    path('test/<int:test_id>/', views.take_test, name='take_test'),
]
