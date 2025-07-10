from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("deals/", views.deals, name="deals"),
    path("create_deal/", views.create_deal, name="create_deal"),
]
