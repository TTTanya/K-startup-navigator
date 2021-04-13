from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact


class ContactForm(ModelForm):

    class Meta:
        # Определяем модель, на основе которой создаем форму
        model = Contact
        # Поля, которые будем использовать для заполнения
        fields = ['email','message']
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите Ваше сообщение'
                }
            ),
            'email': Textarea(
                attrs={
                    'placeholder': 'Напишите Вашу почту',
                    'maxlength': '200',
                    'rows': '2'
                }
            )
        }
