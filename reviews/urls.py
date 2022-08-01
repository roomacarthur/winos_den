
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Reviews.as_view(), name="reviews"),
]
