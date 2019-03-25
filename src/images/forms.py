from django import forms
from django.core.exceptions import ValidationError

# function to limit the file upload size to 5 MB only.
def file_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')

class AddImage(forms.Form):
	title 		= forms.CharField()
	description = forms.CharField(required=False)
	image 		= forms.ImageField(validators=[file_size])
