from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('first', 'second', 'third', 'nation', 'first_translation',
        'second_translation',
        'third_translation'
        )