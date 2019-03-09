from django import forms

class AddImage(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	image 	= forms.ImageField()
	image2 	= forms.ImageField(required=False)
	image3 	= forms.ImageField(required=False)
	image4 	= forms.ImageField(required=False)
	image5 	= forms.ImageField(required=False)
	image6	= forms.ImageField(required=False)
	image7 	= forms.ImageField(required=False)
	image8 	= forms.ImageField(required=False)
	image9 	= forms.ImageField(required=False)
	image10	= forms.ImageField(required=False)