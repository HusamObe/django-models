from django.urls import path
from .views import SnackListView,Snack_Detail

urlpatterns = [
    
    path('',SnackListView.as_view(), name="snacks"),
    path('detail/<pk>',Snack_Detail.as_view(), name="detail"),

]