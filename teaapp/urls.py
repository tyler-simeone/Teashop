from django.urls import path, include
from .views import *

app_name = "teaapp"

urlpatterns = [    
    path('', tea_list, name="tea_list"),
    path('/form/', tea_form, name="tea_form"),
    path('/<int:tea_id>/', tea_details, name="tea_details"),
    path('/<int:tea_id>/form/', tea_edit_form, name="tea_edit_form"),
]
