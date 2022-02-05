from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('Hello World')

def index(request):
    meetups = [
        {'title': 'A first meetup', 'location': 'Abuja', 'slug' : 'a-first-meetup'},
        {'title': 'A Second meetup', 'location': 'Lagos', 'slug': 'a-second-meetup'},
    ]
    return render(request, 'meetups/index.html', {'meetups' : meetups, 'condition': False})


def meetup_details(request, meetup_slug):
    selected_meetup = {
        'title': 'A first Meetup',
        'desc': 'This is our first meetup'
        }
    return render(request, 'meetups/meetup-detail.html', {
        'meetup_detail': selected_meetup
    })
    