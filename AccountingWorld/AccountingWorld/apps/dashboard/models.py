from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Transaction(models.Model):
    """
       Model representing a financial transaction.

       Fields:
           transaction_type (int): Type of transaction, chosen from TRANSACTION_TYPES.
           date (DateField): Date of the transaction.
           amount (FloatField): Amount of the transaction.

       Methods:
           save(*args, **kwargs): Save method to update the journal after saving the transaction.
           update_journal(): Update the journal entries based on the  transaction type
       """

    TRANSACTION_TYPES = (
        (1, 'Sales on cash'),
        (2, 'Sales in credit'),
        (3, 'Expense in cash'),
        (4, 'Expense on credit'),
        (5, 'Client Pays for sales on credit'),
        (6, 'Expense on credit paid'),
        (7, 'Equity Investment'),
        (8, 'Loan'),
        (9, 'Loan repayment'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPES)
    date = models.DateField()
    amount = models.FloatField()

    def save(self, *args, **kwargs):
        """
        Save method to update the journal after saving the transaction.

        This method calls the update_journal method after saving the transaction to create
        corresponding journal entries

        Params:
            args: Variable  length argument list
            kwargs: Arbitrary keyword arguments

        Returns:
            None

        """
        super().save(*args, **kwargs)
        self.update_journal()

    def update_journal(self):
        """
        Update the journal entries based on the transaction  type.

        This method creates journal entries based on the transaction type and updates the journal
        entry related to the transaction

        Params:
            None

        Returns:
            None

        """
        journal_entry = JournalEntry.objects.create(transaction=self)

        if self.transaction_type == 1:
            journal_entry.create_entry('Sales', credit=self.amount, related_account='Bank')
            journal_entry.create_entry('VAT', credit=self.amount * 0.2, related_account='Sales')
            journal_entry.create_entry('Bank', debit=self.amount * 1.2, related_account='Sales')

        elif self.transaction_type == 2:
            journal_entry.create_entry('Sales', credit=self.amount, related_account='Debtors')
            journal_entry.create_entry('VAT', credit=self.amount * 0.2, related_account='Sales')
            journal_entry.create_entry('Debtors', debit=self.amount * 1.2, related_account='Sales')

        elif self.transaction_type == 3:
            journal_entry.create_entry('Expenses', debit=self.amount / 1.2, related_account='Bank')
            journal_entry.create_entry('VAT', debit=(self.amount / 1.2) * 0.2, related_account='Sales')
            journal_entry.create_entry('Bank', credit=self.amount, related_account='Expenses')

        elif self.transaction_type == 4:
            journal_entry.create_entry('Expenses', debit=self.amount / 1.2, related_account='Bank')
            journal_entry.create_entry('VAT', debit=(self.amount / 1.2) * 0.2, related_account='Sales')
            journal_entry.create_entry('Creditors', credit=self.amount, related_account='Expenses')

        elif self.transaction_type == 5:
            journal_entry.create_entry('Debtors', debit=self.amount, related_account='Bank')
            journal_entry.create_entry('Bank', credit=self.amount, related_account='Debtors')

        elif self.transaction_type == 6:
            journal_entry.create_entry('Creditors', debit=self.amount, related_account='Bank')
            journal_entry.create_entry('Bank', credit=self.amount, related_account='Creditors')

        elif self.transaction_type == 7:
            journal_entry.create_entry('Equity', credit=self.amount, related_account='Bank')
            journal_entry.create_entry('Bank', debit=self.amount, related_account='Equity')

        elif self.transaction_type == 8:
            journal_entry.create_entry('Loan', credit=self.amount, related_account='Bank')
            journal_entry.create_entry('Bank', debit=self.amount, related_account='Loan')

        elif self.transaction_type == 9:
            journal_entry.create_entry('Loan', debit=self.amount, related_account='Bank')
            journal_entry.create_entry('Bank', credit=self.amount, related_account='Loan')

    def __str__(self):
        return f"Transaction: {self.id}"


class JournalEntry(models.Model):
    """
    Model representing a journal entry for a transaction

    Fields:
        transaction (ForeignKey): The foreign key to the associated Transaction

    Methods:
        create_entry(account, debit=0, credit=0, related_account=''): Create a journal entry
        for the transaction

    """
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)

    def create_entry(self, account, debit=0, credit=0, related_account=''):
        """
        Create a journal entry for the transaction.

        This method creates a journal entry with the  specified account, debit, credit
        and related account for the associated transaction.


        Params:
            account: The account for the journal entry
            debit: The debit amount for the journal entry Defaults to 0
            credit: The credit amount for the journal entry Defaults to 0
            related_account: The related account for the journal entry Defaults to ''

        Returns:
            None

        """
        Journal.objects.create(
            journal_entry=self,
            account=account,
            debit=debit,
            credit=credit,
            related_account=related_account
        )

    def __str__(self):
        return f"Journal Entry: {self.transaction_id}"


class Journal(models.Model):
    """
    Model representing a single journal entry

    Fields:
        journal_entry (ForeignKey): The foreign key to the associated JournalEntry
        account (CharField): The account for the journal entry
        debit (FloatField): The debit amount for the journal entry
        credit (FloatField): The credit amount for the  journal entry
        related_account (CharField): The related account for the journal entry.

    """
    journal_entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE)
    account = models.CharField(max_length=100)
    debit = models.FloatField(default=0)
    credit = models.FloatField(default=0)
    related_account = models.CharField(max_length=100)

    def __str__(self):
        return f"Journal Entry: {self.journal_entry_id}, Account: {self.account}, Debit: {self.debit}, " \
               f"Credit: {self.credit}, Related Account: {self.related_account}"

