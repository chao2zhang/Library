# Create your views here.
from django import forms
from purchases.models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        exclude = ('paid', 'create_at', 'update_at')