from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('add/',views.add),
    path('update/<int:id>/',views.update )
]