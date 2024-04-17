from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        send_mail(
            "subject",
            "message",
            "user@email.com",
            ["bob@email.com"],
            html_message="<h3 style='font-family: Arial;'>Hello there!</h3><p>Hey! <br> This is our first Email! So excited! ARE YOU??!!</p>",
        )
    except BadHeaderError:
        pass

    return render(request, "hello.html", {"name": "Mosh"})
