from django import forms
from pybo.models import Question, Answer, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {
            "content": "댓글내용",
        }
