from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..models.userModel import User


@login_required(login_url="/login")
def edit_profile(request, id):
    selected_data = User.objects.get(id=id)

    return render(
        request, "pages/edit_profile.html", {"selected_data": selected_data,},
    )


@login_required(login_url="/login")
def update_profile(request):
    id = request.POST["id"]
    name = request.POST["name"]

    if name is not None:
        User.objects.filter(id=id).update(
            name=name
        )
        messages.success(request, "Profile has been updated successfully!")

    else:
        messages.error(request, "Name is required!")

    return redirect("/dashboard")


@login_required(login_url="/login")
def change_password(request, id):
    selected_data = User.objects.get(id=id)

    return render(
        request, "pages/change_password.html", {"selected_data": selected_data,},
    )


@login_required(login_url="/login")
def update_password(request):
    id = request.POST["id"]
    password = request.POST["new_password"]
    confirm_password = request.POST["confirm_password"]

    if password == confirm_password:
        User.objects.filter(id=id).update(password=password,)
        messages.success(request, "Password is changed successfully!")
        return redirect("/dashboard")
    else:
        messages.error(request, "Password is not same!")
        return redirect("/change_password/" + id)
