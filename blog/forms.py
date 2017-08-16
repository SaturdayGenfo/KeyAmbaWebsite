from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=10)
    comment = forms.CharField(widget=forms.Textarea)

class ProverbForm(forms.Form):
    proverb = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)