from django.contrib import admin
from .models import Transaction, JournalEntry, Journal

# Register your models here.
admin.site.register(Transaction)
admin.site.register(JournalEntry)
admin.site.register(Journal)