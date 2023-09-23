from django.urls import path
from . import views

urlpatterns =[
    # users can register through this url # User signup
    path('index/', views.index, name='index'),

    ]