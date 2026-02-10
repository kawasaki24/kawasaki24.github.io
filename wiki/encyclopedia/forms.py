from django import forms

class Search(forms.Form):
    q = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Search', 
            'autocomplete': 'off',
            }),
    )


class Create_page(forms.Form):
    title = forms.CharField(
        label="Title", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'autofocus': True
            }),
        required=True
    )
    content = forms.CharField(
        widget=forms.Textarea,
        required=True
    )
    

class Edit_page(forms.Form):
    title = forms.CharField(
        label="Title",
        disabled=True,
        required=False
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'autofocus': True
        }),
        required=True,
    )