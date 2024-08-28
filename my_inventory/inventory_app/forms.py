from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id' : 'Product ID',
            'product_name' : 'Product Name',
            'sku' : 'SKU',
            'price' : 'Price',
            'quantity' : 'Quantity',
            'supplier' : 'Supplier',
        }
        widgets = {
            'product_id' : forms.NumberInput(attrs={
                'placeholder' : 'e.g 1', 'class' : 'text-sm font-medium leading-5 rounded-md placeholder-gray-900 text-gray-700 w-full'
            }),
            
             'product_name' : forms.TextInput(attrs={
                'placeholder' : 'e.g jeans', 'class' : 'text-sm font-medium leading-5 rounded-md placeholder-gray-900 text-gray-700 w-full'
            }),

             'sku' : forms.TextInput(attrs={
                'placeholder' : 'e.g SK123', 'class' : 'text-sm font-medium leading-5   rounded-md placeholder-gray-900 text-gray-700 w-full'
            }),

             'price' : forms.NumberInput(attrs={
                'placeholder' : 'e.g 100.10', 'class' : 'text-sm font-medium leading-5  rounded-md placeholder-gray-900 text-gray-700 w-full'
            }),

             'quantity' : forms.NumberInput(attrs={
                'placeholder' : 'e.g 5', 'class' : 'text-sm font-medium leading-5  rounded-md placeholder-gray-900 text-gray-700 w-full'
            }),

             'supplier' : forms.TextInput(attrs={
                'placeholder' : 'e.g XYZ', 'class' : 'text-sm font-medium leading-5  rounded-md placeholder-gray-900 text-gray-700 w-full'
            }),
        }