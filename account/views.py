from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def account(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('account')

    else:
        return render(request, 'account/account.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['reset_password_token']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name,
                                                      last_name=last_name)
                user.save()

                from django.core.mail import EmailMessage
                from django.conf import settings
                from django.template.loader import render_to_string

                template = render_to_string('account/email_send_template.html', {'user': user})

                email = EmailMessage(
                    'Thanks for subscribing to us!',
                    template,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                )
                email.send()

                return redirect('account')

        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'account/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
