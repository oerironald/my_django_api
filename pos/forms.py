from django import forms
from .models import Product, Customer

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'unit']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Product.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("A product with this name already exists.")
        return name

class IndividualProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    quantity = forms.DecimalField(max_digits=10, decimal_places=2)

class PaymentForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    payment_method = forms.ChoiceField(choices=[('cash', 'Cash'), ('mpesa', 'Mpesa')])

# Formset for multiple products
ProductFormSet = forms.formset_factory(IndividualProductForm, extra=1)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email']
