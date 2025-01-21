
from django.urls import path
from . import views

urlpatterns = [
    path('content/<str:page>', views.content, name="content"),
]

