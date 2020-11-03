from django import forms
from . models import Posts


class PostsForm(forms.ModelForm):
	class Meta:
		model = Posts 
		fields = ('text', 'image', 'video',)

		widgets = {
			'text':forms.Textarea({'placeholder':'Ubaci opis...ili ne', 'rows':1, 'cols':40})
		}
		