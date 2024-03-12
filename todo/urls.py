from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("create-user", views.create_user, name="create-user"),
]
