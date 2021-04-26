from django.contrib import admin
from django.urls import path
from .views import userViews, courierViews, loginViews, profileViews
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", loginViews.user_login, name="logIn"),
    path("dashboard", userViews.dashboard, name="dashboard"),

    path("user", userViews.user, name="user"),
    path("create_user", userViews.create_user, name="create_user"),
    path("edit_user/<int:id>", userViews.edit_user, name="edit_user",),
    path("update_user", userViews.update_user, name="update_user",),
    path("delete_user/<int:id>", userViews.delete_user, name="delete_user",),

    path("courier", courierViews.courier, name="courier"),
    path("create_order", courierViews.create_order, name="create_courier"),
    path("delete_order/<int:id>", courierViews.delete_order, name="delete_courier",),


    path("login", loginViews.user_login, name="user_login",),
    path("logout", loginViews.user_logout, name="user_logout",),
    path("edit_profile/<int:id>", profileViews.edit_profile, name="edit_profile",),
    path("update_profile", profileViews.update_profile, name="update_profile",),
    path(
        "change_password/<int:id>",
        profileViews.change_password,
        name="change_password",
    ),
    path("update_password", profileViews.update_password, name="update_password",),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
