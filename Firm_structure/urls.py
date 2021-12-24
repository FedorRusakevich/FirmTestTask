from django.urls import path

from . import views


urlpatterns = [
    path("employee/", views.AllEmployeesList.as_view()),
]