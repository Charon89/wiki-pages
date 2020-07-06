from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entryName>", views.entry, name="entry"),
    path("edit/<str:entryName>", views.edit, name="edit"),
]
