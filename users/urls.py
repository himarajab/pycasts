from django.urls import path
from . import views

app_name = "user"   


urlpatterns = [
    path('register/', views.RegisterAPI.as_view(), name='register'),

]