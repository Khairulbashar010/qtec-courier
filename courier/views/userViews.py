from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import redirect, render
from django.contrib import messages

from ..models.orderModel import Order
from ..models.userModel import User


@login_required(login_url="/login")
def dashboard(request):
    current_user = request.user
    total_user_number = User.objects.all().filter(is_superuser=False).count()
    if current_user.is_superuser:
        total_order_number = Order.objects.all().order_by("-id").select_related('merchant').count()
    else:
        total_order_number = Order.objects.all().filter(order_from=current_user.id).order_by("-id").select_related("merchant").count()
    return render(
        request,
        "pages/dashboard.html",
        {
            "total_user_number": total_user_number,
            "total_order_number": total_order_number,
        },
    )


@login_required(login_url="/login")
def user(request):
    all_user_data = User.objects.all().filter(is_superuser = False)

    return render(
        request,
        "pages/user.html",
        {
            "all_user_data": all_user_data,
        },
    )


@login_required(login_url="/login")
def create_user(request):

    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]

    if name == "":
            messages.error(request, "All fields are required")
            return redirect("/user")
    if email == "":
            messages.error(request, "All fields are required")
            return redirect("/user")
    if password == "":
            messages.error(request, "All fields are required")
            return redirect("/user")

    try:
        validate_email( email )
        user = User(
            name=name,
            email=email,
            password=password,
        )
        user.password = make_password(password)
        user.save()
        messages.success(request, "User has been created successfully!")

    except ValidationError:
        messages.error(request, "Enter a valid e-mail address.")

    return redirect("/user")


@login_required(login_url="/login")
def edit_user(request, id):
    all_user_data = User.objects.all()
    selected_data = User.objects.get(id=id)

    return render(
        request,
        "pages/user.html",
        {
            "all_user_data": all_user_data,
            "selected_data": selected_data,
        },
    )


@login_required(login_url="/login")
def update_user(request):
    id = request.POST["id"]
    name = request.POST["name"]
    email = request.POST["email"]
    password = request.POST["password"]

    if name == "":
            messages.error(request, "All fields are required")
            return redirect("/user")
    if email == "":
            messages.error(request, "All fields are required")
            return redirect("/user")

    if password == "":
        User.objects.filter(id=id).update(
            name=name,
            email=email,
        )
        messages.success(request, "User has been updated successfully!")
        return redirect("/user")
    else:
        password = make_password(password)
        User.objects.filter(id=id).update(
            name=name,
            email=email,
            password=password,
        )
        messages.success(request, "User has been updated successfully!")
        return redirect("/user")

    return redirect("/user")


@login_required(login_url="/login")
def delete_user(request, id):
    obj = User.objects.get(id=id)
    obj.delete()
    messages.error(request, "User Removed!")
    return redirect("/user")
