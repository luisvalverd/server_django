
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Products

class CreateProductForm(ModelForm):
    def clean_name(self):
        data = self.cleaned_data['name']

        if data == "":
            raise ValidationError(_("Invalid name - name is void"))

        return data
    
    def clean_price(self):
        data = self.cleaned_data['price']

        if data == 0:
            raise ValidationError(_("Invalid price - price is 0"))
        
        if data < 0:
            raise ValidationError(_("Invalid price - price is a value negative"))
        
        return data
    
    def clean_stock(self):
        data = self.cleaned_data['stock']

        if data == 0:
            raise ValidationError(_("Invalid stock - stock is 0"))

        if data < 0:
            raise ValidationError(_("Invalid stock - stock is a value negative"))

        return data

    class Meta:
        model = Products
        fields = '__all__'

