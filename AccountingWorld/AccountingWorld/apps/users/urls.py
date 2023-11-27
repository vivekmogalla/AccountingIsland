from django.urls import path
from . import views

urlpatterns = [
    # users can register through this url # User signup
    path('signup/', views.SignupPageView.as_view(), name='signup'),

    # user receive activate token on first time registration
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),

    # users can log in through this url # User Login
    path('login/', views.LoginPageView.as_view(), name='login'),

    # uses can log out through this url # User Logout
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
