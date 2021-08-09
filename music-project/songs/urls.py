from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.apiOverview,name="overview"),
    path('list/',views.lists,name="lists"),
    path('detail/',views.details,name="details"),
    path('create/',views.create,name="create"),

]