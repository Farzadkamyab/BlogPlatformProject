from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class UpdateCommentForm(forms.Form):
    content = forms.CharField(max_length = 200)