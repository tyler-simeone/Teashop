from django.urls import path, include
# from teaapp import views
from .views import *

app_name = "teaapp"

urlpatterns = [
    path('/', tea_list, name="tea_list"),
    # path('/', tea_list, name="tea_list"),
]
