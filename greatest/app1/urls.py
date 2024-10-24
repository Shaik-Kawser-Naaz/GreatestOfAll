from django.urls import path
from app1 import views

urlpatterns=[
    path('great',views.func1,name="gn")
]
