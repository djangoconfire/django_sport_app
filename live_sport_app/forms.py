from django import forms
from models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=['order_id','product_name','order_status','product_url','price']

        labels={
            'order_id':'Order Id',
            'product_name':'Product Name',
            'order_status':'Order Status',
            'product_url':'Product Url',
            'price':'Cost Price'
        }

        widgets={
            'order_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Order Id'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}),
            'product_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Url'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Cost Price'})
        }