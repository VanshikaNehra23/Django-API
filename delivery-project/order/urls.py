from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.apiOverview,name="apiOverview"),
    path('add-details/', views.add_details,name="add_details"),
    path('get-details/', views.get_details,name="get_details"),
    path('add-order/',views.add_order,name="add_order"),
    path('get-order/',views.get_order,name="get_order"),
    path('update-order/<str:name>/',views.update_order,name="update_order"),
    path('show/',views.show,name='show')
]