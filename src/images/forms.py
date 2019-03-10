from django import forms


class AddImage(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	image 		= forms.ImageField()
