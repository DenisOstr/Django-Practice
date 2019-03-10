from django import forms

class UsersForm(forms.Form):
	FirstName = forms.CharField(max_length = 200)
	LastName = forms.CharField(max_length = 200)
	Email = forms.CharField(max_length = 200)