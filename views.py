from django.shortcuts import render
from .models import Task
from .forms import UserForm
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def section1(request):
    return render(request, 'main/section1.html')


def section2(request):
    return render(request, 'main/section2.html')


def section3(request):
    return render(request, 'main/section3.html')


def section4(request):
    return render(request, 'main/section4.html')


def section5(request):
    return render(request, 'main/section5.html')


def section6(request):
    return render(request, 'main/section6.html')


def section7(request):
    return render(request, 'main/section7.html')


def test(request):
    return render(request, 'main/test.html')


class ContactCreate(CreateView):
    model = Contact
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы, почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'starsplus.team@gmail.com',
      ['starsplus.team@gmail.com']
   )

# Функция, которая вернет сообщение в случае успешного заполнения формы
def success(request):
   return HttpResponse('Ваше письмо успешно отправлено.')
