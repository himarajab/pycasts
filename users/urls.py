from django.urls import path
from . import views
from knox import views as knox_views

app_name = "user"   


urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logout_all/', knox_views.LogoutAllView.as_view(), name='logout_all'),

]