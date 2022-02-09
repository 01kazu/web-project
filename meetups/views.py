from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegistrationForm
from .models import Meetup, Participant

# Create your views here.

# def index(request):
#     return HttpResponse('Hello World')

def index(request):
    # meetups = [
    #     {'title': 'A first meetup', 'location': 'Abuja', 'slug' : 'a-first-meetup'},
    #     {'title': 'A Second meetup', 'location': 'Lagos', 'slug': 'a-second-meetup'},
    # ]
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups' : meetups, 'condition': False})


def meetup_details(request, meetup_slug):
    # selected_meetup = {
    #     'title': 'A first Meetup',
    #     'desc': 'This is our first meetup'
    #     }
    try:
        selected_meetup  = Meetup.objects.get(slug = meetup_slug)
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                participant = form.save()
                selected_meetup.participants.add(participant)
                return redirect('meetup-confirmation', meetup_slug=meetup_slug, confirm="success")
        else:
            form = RegistrationForm()
        return render(request, 'meetups/meetup-detail.html', {
            'meetup_detail': selected_meetup,
            'meetup_found': True,
            'form' : form,
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-detail.html', {
            'meetup_found': False,
        })


def meetup_confirmation(request, meetup_slug, confirm):
    meetup  = Meetup.objects.get(slug = meetup_slug)
    webpage_info = {
        'meetup': meetup,
        'confirm': confirm,
    }
    return render(request, 'meetups/meetup-confirmation.html', webpage_info)

    