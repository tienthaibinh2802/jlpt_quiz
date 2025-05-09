from django import forms
from .models import Comment

class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)

        for question in questions:
            choices = [(option.id, option.text) for option in question.options.all()]
            self.fields[f"question_{question.id}"] = forms.ChoiceField(
                label=question.content,
                choices=choices,
                widget=forms.RadioSelect,
                required=True
            )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 3}),
        }