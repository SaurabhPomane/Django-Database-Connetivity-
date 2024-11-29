from django.urls import path
from secondapp import views

urlpatterns = [
    path('first/',views.first),
    path('calculator/',views.calculator),
    path('result/',views.result),
    path('save/',views.save),
    path('',views.login),
    path("display/",views.display),
    path("delete/<usernamebr>",views.delete),
    path("crud_operation/",views.crud_operation),
    path('givestudentdetail/',views.givestudentdetail)
]