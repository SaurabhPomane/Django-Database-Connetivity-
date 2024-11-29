from django.urls import path
from testapp import views

urlpatterns=[
  path('hellow/',views.hellow),
  path('hi/',views.hi),
  path('add/',views.add),
  path('GiveMePage/',views.GiveMePage),
  path('save/',views.save),
  path('login/',views.login),
  path('display_data/',views.display_data),
  path('delete/<usernamefrombrouser>',views.delete),
  path('crudoperation/',views.crudoperation),
  path('view/',views.view),
  path('add/',views.add),
  path('update/',views.update),
  path('delette/',views.delette),
  path('setSession/',views.setSession),
  path('increase/',views.increase),
  path('check/',views.check),
  path('aggration/',views.aggration),
  path('saveUserData/',views.saveUserData),
  path('login2/',views.login2),
  path('generateForm/',views.generateForm),
  path('show/',views.show)

]