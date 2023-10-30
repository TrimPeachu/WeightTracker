from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.getUsers),
    path('users/', views.getUsers),
    path('user/<str:pk>/', views.getUser),
    # path('login/', views.loginUser),
    path('login/<str:username>/<str:password>/', views.loginUser),
    path('users/create/', views.createUser),
    path('user/<str:pk>/update/', views.updateUser),
    path('user/<str:pk>/delete/', views.deleteUser),
    path('weights/', views.getWeights),
    path('weights/<str:pk>/', views.getUserWeights),
    path('weight/add/', views.addWeight),
    path('weight/<str:pk>/update/', views.updateWeight),
    path('weight/<str:pk>/delete/', views.deleteWeight),
]
