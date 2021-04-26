from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..models.orderModel import Order
from ..models.userModel import User


@login_required(login_url="/login")
def courier(request):
    current_user = request.user
    all_user_data = User.objects.all().filter(is_superuser=False)
    if current_user.is_superuser:
        all_order_data = Order.objects.all().order_by("-id").select_related('merchant')
    else:
        all_order_data = Order.objects.all().filter(order_from=current_user.id).order_by("-id").select_related("merchant")

    return render(
        request,
        "pages/courier.html",
        {
            "all_user_data": all_user_data,
            "all_order_data": all_order_data,
        },
    )


@login_required(login_url="/login")
def create_order(request):
    order_from = request.user.id
    merchant_id = request.POST["merchant"]
    product_type = request.POST["product_type"]
    invoice_id = request.POST["invoice_id"]
    location = request.POST["location"]
    weight = request.POST["weight"]
    total = request.POST["total"]

    if merchant_id == "":
            messages.error(request, "Select a Merchant")
            return redirect("/courier")
    if product_type == "":
            messages.error(request, "Select a Type ")
            return redirect("/courier")
    if invoice_id == "":
            messages.error(request, "Provide Invoice ID")
            return redirect("/courier")
    if location == "":
            messages.error(request, "Select a Location ")
            return redirect("/courier")
    if weight == "":
            messages.error(request, "Select Weight ")
            return redirect("/courier")


    order = Order(
        order_from=order_from,
        merchant_id=merchant_id,
        product_type=product_type,
        invoice_id=invoice_id,
        location=location,
        weight=weight,
        total=total,
    )

    order.save()
    messages.success(request, "Order created successfully!")

    return redirect("/courier")

@login_required(login_url="/login")
def delete_order(request, id):
    obj = Order.objects.get(id=id)
    obj.delete()
    messages.error(request, "Order deleted!")
    return redirect("/courier")
