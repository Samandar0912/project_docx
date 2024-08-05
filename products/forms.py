from .models import Product
from django import forms 

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'categoryScience', 'name', 'price', 'file')

    def save(self, request, commit=True):
        product = super().save(commit=False)  # commit=False bilan saqlashni keyinroq qilamiz
        product.Author = request.user
        if commit:
            product.save()  # commit=True bo'lsa, saqlaymiz
        return product
    
    
class ProdctForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','categoryScience','name','price','file')