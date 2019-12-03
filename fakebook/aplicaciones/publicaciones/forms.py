from django import forms
from .models import Post

class PostForm(forms.ModelForm):


	class Meta:
		model = Post 
		fields = ['content', 'image', 'author']
		widgets = {
			'content': forms.Textarea(attrs={'class':'form-control'}),
			'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
			'author': forms.Select(attrs={'class':'input-group-text'})
			}
		labels = {
			'content':'','image':'','author':''
		}