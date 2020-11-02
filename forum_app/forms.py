from django import forms
from . models import Posts


class PostsForm(forms.ModelForm):
	class Meta:
		model = Posts 
		fields = ('text', 'image', 'video',)

		widgets = {
			'text':forms.Textarea({'placeholder':'Add some description here...or not', 'rows':1, 'cols':40})
		}
		