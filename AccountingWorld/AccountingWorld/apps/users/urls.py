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

    # users can reset their password through this url # Password Reset # clear to me
    path('password-reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),

    # users confirmation password reset through this url # Password Reset Confirmation # clear to me
    path('password-reset/done', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),

    # users password reset activation token through this url # Password Reset Activation Token
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    # users password reset complete
    path('password-reset-complete/', views.CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
