from django import forms
from .models import Order, User


# class TaskForm(forms.Form):
#     text = forms.CharField(
#         max_length=20
#     )
#     checked = forms.BooleanField(required=False)
class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'FIO',
            'phone_number',
            'location',
            'email',
            'password',
        ]


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'weight',
            'order_name',
            'getter'
        ]

    def clean(self):
        text = self.data['text']
        if text == 'text':
            raise forms.ValidationError(
                {
                    'text': 'mistake text'
                }
            )