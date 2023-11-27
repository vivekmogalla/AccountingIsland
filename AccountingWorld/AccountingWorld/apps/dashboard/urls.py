from django.urls import path
from . import views

urlpatterns =[
    # Application urls
    path('', views.AddTransactionView.as_view(), name='dashboard'),

    path('transactions/add', views.AddTransactionView.as_view(),  name='add_transaction'),

    path('transactions/list/', views.TransactionListView.as_view(), name='transaction_list'),

    path('transactions/calculate_profit_loss/', views.calculate_profit_loss_function, name='calculate_profit_loss'),

    path('transactions/get_balance_sheet/', views.get_balance_sheet, name='get_balance_sheet'),

    path('transactions/cash_flow_data/', views.get_cash_flow, name='get_cashflow_data'),

    path('reset_transactions/', views.reset_transactions, name='reset_transactions'),

    ]