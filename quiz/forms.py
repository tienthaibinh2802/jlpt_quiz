from django import forms

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
