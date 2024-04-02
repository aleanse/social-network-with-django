from django import forms
from user.models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
     title = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Title'}))
     text_post = forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder':'Text'}))
     image = forms.FileField(required=False)


     
     class Meta: # especifica o modelo e os campos do modelo que serão usados
        model = Post
        fields = ['title','text_post','image']
