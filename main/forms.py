from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('first', 'second', 'third')
        nation_name = forms.CharField(max_length=100,)