from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView
from dj_rest_auth.views import LoginView, LogoutView


app_name = "user"   

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]

