from django import forms

class ReviewForm(forms.Form):
    name = forms.CharField(label='Firstname', min_length=3, max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'E-mail', 'id': 'form-email'}))
    review = forms.CharField(label='Review', widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '5'}))
    

