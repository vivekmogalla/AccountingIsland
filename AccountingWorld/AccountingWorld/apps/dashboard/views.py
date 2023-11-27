from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.db.models import Sum
from .models import Journal, Transaction
from collections import defaultdict


class AddTransactionView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ['transaction_type', 'date', 'amount']
    template_name = 'dashboard/add_transactions.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.transaction_type = int(form.instance.transaction_type)
        form.instance.amount = float(form.instance.amount)

        # Check if the 'date', 'transaction_type', or 'amount' fields are empty
        errors = {}
        if not form.cleaned_data.get('date'):
            errors['date'] = 'Please provide a date for the transaction.'
        if not form.cleaned_data.get('transaction_type'):
            errors['transaction_type'] = 'Please select a transaction type.'
        if not form.cleaned_data.get('amount'):
            errors['amount'] = 'Please enter the amount.'

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        response = super().form_valid(form)
        # messages.success(self.request, 'Transaction added successfully')
        return JsonResponse({'message': 'Transaction added successfully'})

    def get_success_url(self):
        return reverse('dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['showback'] = True
        return context


class TransactionListView(LoginRequiredMixin, ListView):
    model = Journal
    template_name = 'dashboard/transaction_list.html'
    paginate_by = 20
    context_object_name = 'journals'

    # @silk_profile(name='Transaction List View')
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        account = self.request.GET.get('account')

        # Filter transactions based on the logged-in user and use select_related()
        queryset = queryset.select_related('journal_entry__transaction').filter(
            journal_entry__transaction__user=self.request.user)

        if account:
            queryset = queryset.filter(account__iexact=account)
        return queryset


def calculate_profit_loss(user):
    # Sample output will be {'total_credit': 700.0, 'total_debit': 800} for the line  below

    # fetch the info related to logged-in user
    sales = Journal.objects.filter(journal_entry__transaction__user=user, account='Sales'). \
        select_related('journal_entry__transaction').aggregate(total_credit=Sum('credit'), total_debit=Sum('debit'))
    sales_credit = sales['total_credit'] or 0
    sales_debit = sales['total_debit'] or 0

    expenses = (Journal.objects.filter(journal_entry__transaction__user=user, account='Expenses').
                select_related('journal_entry__transaction').aggregate(total_credit=Sum('credit'),
                                                                       total_debit=Sum('debit')))
    expenses_credit = expenses['total_credit'] or 0
    expenses_debit = expenses['total_debit'] or 0

    # Calculate the total expenses
    sales = sales_credit - sales_debit
    expenses = expenses_debit - expenses_credit
    profit_loss = sales - expenses

    return sales, expenses, profit_loss


def calculate_profit_loss_function(request):
    # Calculate profit loss data here
    sales, expenses, profit_loss = calculate_profit_loss(request.user)

    # Create a dictionary with the profit loss data
    data = {
        'sales': sales,
        'expenses': expenses,
        'profit_loss': profit_loss,
    }

    # Return the data as JSON response
    return JsonResponse(data)


def balance_sheet_view(user):
    try:
        expenses = Journal.objects.filter(journal_entry__transaction__user=user, account='Expenses').select_related(
            'journal_entry__transaction').aggregate(
            total_credit=Sum('credit'), total_debit=Sum('debit')
        )

        expenses_credit = expenses['total_credit'] or 0
        expenses_debit = expenses['total_debit'] or 0

        expenses_credit = round(expenses_credit, 2)
        expenses_debit = round(expenses_debit, 2)

        # select related queryy
        sales = Journal.objects.filter(journal_entry__transaction__user=user, account='Sales').select_related(
            'journal_entry__transaction').aggregate(
            total_credit=Sum('credit'), total_debit=Sum('debit')
        )

        sales_credit = sales['total_credit'] or 0
        sales_debit = sales['total_debit'] or 0

        sales_credit = round(sales_credit, 2)
        sales_debit = round(sales_debit, 2)

        sales = sales_credit - sales_debit
        expenses = expenses_debit - expenses_credit
        profit = sales - expenses

        # get the bank balance
        # select related queryy
        bank_balance = Journal.objects.filter(journal_entry__transaction__user=user, account='Bank').select_related(
            'journal_entry__transaction').aggregate(
            total_credit=Sum('credit'), total_debit=Sum('debit')
        )

        bank_balance = (bank_balance['total_debit'] or 0) - (bank_balance['total_credit'] or 0)
        bank_balance = round(bank_balance, 2)
        # bank_balance = (bank_balance['total_credit'] or 0) - (bank_balance['total_debit'] or 0)

        # get the debtors balance
        # select related queryy
        debtors_balance = Journal.objects.filter(journal_entry__transaction__user=user,
                                                 account='Debtors').select_related(
            'journal_entry__transaction').aggregate(
            total_credit=Sum('credit'), total_debit=Sum('debit')
        )
        debtors_balance = (debtors_balance['total_debit'] or 0) - (debtors_balance['total_credit'] or 0)

        debtors_balance = round(debtors_balance, 2)
        # get the creditors balance
        # select related query
        creditors_balance = Journal.objects.filter(journal_entry__transaction__user=user,
                                                   account='Creditors').select_related(
            'journal_entry__transaction').aggregate(
            total_credit=Sum('credit'), total_debit=Sum('debit'))
        creditors_balance = (creditors_balance['total_credit'] or 0) - (creditors_balance['total_debit'] or 0)
        creditors_balance = round(creditors_balance, 2)

        # get the vat balance
        # select related queryy
        vat_balance = Journal.objects.filter(journal_entry__transaction__user=user,
                                             account='VAT').select_related('journal_entry__transaction'). \
            aggregate(total_credit=Sum('credit'), total_debit=Sum('debit'))
        vat_balance = (vat_balance['total_credit'] or 0) - (vat_balance['total_debit'] or 0)
        vat_balance = round(vat_balance, 2)

        # get the load balance
        # select related query
        loan_balance = Journal.objects.filter(journal_entry__transaction__user=user,
                                              account='Loan').select_related('journal_entry__transaction'). \
            aggregate(total_credit=Sum('credit'), total_debit=Sum('debit'))
        loan_balance = (loan_balance['total_credit'] or 0) - (loan_balance['total_debit'] or 0)
        loan_balance = round(loan_balance, 2)

        # get the  equity balance
        # select related query
        equity_balance = Journal.objects.filter(journal_entry__transaction__user=user,
                                                account='Equity').select_related('journal_entry__transaction'). \
            aggregate(total_credit=Sum('credit'), total_debit=Sum('debit'))
        equity_balance = (equity_balance['total_credit'] or 0) - (equity_balance['total_debit'] or 0)
        equity_balance = round(equity_balance, 2)

        retained_earnings = sales - expenses

        # Calculate total assets and liabilities
        total_assets = bank_balance + debtors_balance
        total_liabilities_equity = creditors_balance + vat_balance + loan_balance + equity_balance + retained_earnings

        context = {
            'bank_balance': bank_balance,
            'debtors_balance': debtors_balance,
            'vat_balance': vat_balance,
            'creditors_balance': creditors_balance,
            'loan_balance': loan_balance,
            'equity_balance': equity_balance,
            'retained_earnings': retained_earnings,
            'total_assets': total_assets,
            'total_liabilities_equity': total_liabilities_equity,
        }

        return context

    except Exception as e:
        print(f"The exception caused is {e}")


def get_balance_sheet(request):
    # get balance sheet information
    balance_sheet_data = balance_sheet_view(request.user)
    return JsonResponse(balance_sheet_data, safe=False)


def cashflow(user):
    bank_transactions = Journal.objects.filter(journal_entry__transaction__user=user, account='Bank')

    converted_data = []
    for entry in bank_transactions:
        converted_entry = {
            'Account': entry.account,
            'Debit': entry.debit,
            'Credit': entry.credit,
            'Related Account': entry.related_account,
        }
        converted_data.append(converted_entry)

    # Now 'converted_data' contains the list of dictionaries
    # Create a defaultdict to group entries by 'Related Account'
    grouped_data = defaultdict(lambda: {'Account': '', 'Debit': 0.0,
                                        'Credit': 0.0, 'Related Account': '', 'Total': ''})

    # Iterate through the list_data and aggregate the values by 'Related Account'
    for entry in converted_data:
        related_account = entry['Related Account']
        debit = entry['Debit']
        credit = entry['Credit']
        total = entry['Debit'] - entry['Credit']

        grouped_data[related_account]['Account'] = entry['Account']
        grouped_data[related_account]['Debit'] += debit
        grouped_data[related_account]['Credit'] += credit
        grouped_data[related_account]['Related Account'] = related_account
        grouped_data[related_account]['Total'] =grouped_data[related_account]['Debit'] - grouped_data[related_account]['Credit']

    cashflow_data_dict = list(grouped_data.values())
    context = {'cashflow_data': cashflow_data_dict}

    return context


def get_cash_flow(request):
    # get cash flow information
    cashflow_info = cashflow(request.user)
    cashflow_info = cashflow_info['cashflow_data']
    return JsonResponse(cashflow_info, safe=False)


def reset_transactions(request):
    try:
        # Delete all transactions from the database
        Transaction.objects.all().delete()
        return JsonResponse({'message': 'Transaction reset successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=200)