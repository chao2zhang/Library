# Create your views here.here.
from django import forms
from library.sales.models import Sale

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        exclude = ('create_at', 'update_at')