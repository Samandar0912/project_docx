from .models import Product
from django import forms 

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'categoryScience', 'name', 'price', 'file')

    def save(self, request, commit=True):
        product = self.instance
        product.Author = request.user
        super().save(commit)
        return product
    
    
class ProdctForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','categoryScience','name','price','file')