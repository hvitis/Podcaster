from django.shortcuts import render
from django.http import HttpResponseRedirect
from joinnewsletter.forms import JoinForm
from django.contrib import messages
from django.core.mail import EmailMessage

def newsletter(request):
    # This function is called by just a simple url in template
    if request.method == 'POST':
        newsletter_form = JoinForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            #TODO: Send e-mail on new subscriber
            success_msg = "You have been subscribed to the newsletter! Congratz!"
            messages.success(request, success_msg)
            print(success_msg)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "There was an error while subscribing!")
            return HttpResponseRedirect('/')
    else:
        # Rendering newsletter_form on GET
        newsletter_form = JoinForm()
        content = {
            "newsletter_form": newsletter_form
        }
        return render(request, 'base.html', content)
