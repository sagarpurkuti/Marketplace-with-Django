from django import forms
from .models import Item  # Adjusted to import the correct model

INPUT_CLASSES='w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:  # 'Meta' should start with an uppercase letter
        model = Item  # Corrected the model name to 'Item'
        fields = ('Category', 'name','price','description', 'image',)  # Adjusted the tuple of fields
        widgets={
            'Category': forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:  # 'Meta' should start with an uppercase letter
        model = Item  # Corrected the model name to 'Item'
        fields = ( 'name','price','description', 'image','is_sold')  # Adjusted the tuple of fields
        widgets={
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
        }



    

