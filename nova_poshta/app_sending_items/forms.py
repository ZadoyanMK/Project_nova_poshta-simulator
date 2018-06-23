from django import forms
from .models import Order


class TaskForm(forms.Form):
    text = forms.CharField(
        max_length=20
    )
    checked = forms.BooleanField(required=False)


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'weight',
            'order_name',
            'getter',
            'transporting'
        ]
        labels = {
            'text': 'Input text here'
        }

    def clean(self):
        text = self.data['text']
        if text == 'text':
            raise forms.ValidationError(
                {
                    'text': 'mistake text'
                }
            )