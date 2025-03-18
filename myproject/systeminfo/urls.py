from django.urls import path
from .views import htop

urlpatterns = [
    path('htop/', htop),
]
