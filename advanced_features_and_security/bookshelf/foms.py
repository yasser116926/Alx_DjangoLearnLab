from django import forms
from .models import Book

# Form for creating/updating Book instances
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Add any other fields as needed

# Example form for testing purposes
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Message")