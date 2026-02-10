from django.urls import path

from . import views

urlpatterns = [
    # when visiting 127.0.0.1:8000, go into the views.py file and call the index function
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("wiki/<str:title>/", views.content, name="content"),
    path("create_new_page/", views.create, name="create"),
    path("random_page/", views.random_pages, name="random"),
    path("wiki/<str:title>/edit_page/", views.edit, name="edit")
]
