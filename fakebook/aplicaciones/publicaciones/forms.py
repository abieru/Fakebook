from django import forms
from .models import Post

class PostForm(forms.ModelForm):


	class Meta:
		model = Post 
		fields = ['title', 'content', 'image', 'author']
		widgets = {
			'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
			'content': forms.Textarea(attrs={'class':'form-control'}),
			'image': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
			}
		labels = {
			'title':'','content':'','image':'','author':'Hecho por:'
		}