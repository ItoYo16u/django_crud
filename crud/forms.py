from django.forms import ModelForm
from .models import householdAccount

class householdAccountForm(ModelForm):
    class Meta:
        model = householdAccount
        fields =("item","price","category","memo")


