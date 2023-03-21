import smtplib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddPostForm


def index(request):
    date = {
        'title': 'Welcome!',
    }
    return render(request, 'main/index.html', date)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    form = AddPostForm()
    if request.method == 'POST':
        title = request.POST['title']
        email = request.POST['email']
        number = request.POST['number']
        text = request.POST['text']
        my_email = "tima_holl@mail.ru"
        password = "qfyLrAV7wRpaQ6AQQDFw"
        with smtplib.SMTP("smtp.mail.ru") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="tima_holl@mail.ru",
                                msg=f"Subject:You have a new order!\n\nMy name is {title}\n{text}\n{email}\n{number}"
                                )
        return redirect('about')
    return render(request, 'main/contact.html', {'form': form})
