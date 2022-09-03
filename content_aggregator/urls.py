from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("", include("podcasts.urls")),
    path('admin/', admin.site.urls),
    path('user/', include("users.urls")),

]
