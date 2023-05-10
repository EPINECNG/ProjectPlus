from django.urls import path

from . import views

app_name = "accounts"
"""Defining a url path"""


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("sign_up/", views.sign_up_request, name="sign_up"),
]
