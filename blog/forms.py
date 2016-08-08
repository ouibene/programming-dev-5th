from django import forms
from blog.models import Comment, Post


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'message', 'jjal']


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'created_at']
