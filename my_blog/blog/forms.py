from django import forms
from blog.models import Post, Comment

class PostForm(forms.Model):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea postcontent'})
        }

class CommentsForm(forms.Model):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs = {'class': 'textinputclass'}),
            'text': forms.Textarea(attrs = {'class': 'editable medium-editor-textarea'})
        }
