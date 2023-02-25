from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('signup/', views.SignupView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('main/', views.MainView, name='list'),
    path('admin/', admin.site.urls)
]

"""
urlpatterns = [
    path('detail/<int:pk>/', views.detailview, name='detail'),
    path('create/', views.CreateClass.as_view(), name='create')
]
"""