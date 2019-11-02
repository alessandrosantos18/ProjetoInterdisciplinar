from django.urls import path
from AppOlaMundo.views import Index

urlpatterns = [
    path('',Index.as_view(), name="index"),
]
