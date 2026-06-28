from django.contrib import admin
from django.urls import path
from eventApp import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.index, name="home"),
    path("event/<int:id>/", views.details, name="details"),
    path("register/<int:id>/", views.register, name="register"),
    path("registrations/", views.registrations, name="registrations"),
    path("cancel/<int:id>/", views.cancel, name="cancel"),
]