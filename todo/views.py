from django.shortcuts import render
from .forms import CreateUserForm


def create_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        pass

    context = {"form": form}
    return render(request, "todo/create-user.html", context)
