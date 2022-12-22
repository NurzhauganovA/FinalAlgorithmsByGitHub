from .models import Comment
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = [
                'title',
                'post_name',
                'author',
                'text',
        ]

        widgets = {
            "author_name": TextInput(attrs={
                'class': 'write_comment_title',
                'placeholder': 'Comment Title'
            }),
            "full_text": Textarea(attrs={
                'class': 'write_comment_description',
                'placeholder': 'Comment description'
            })
        }