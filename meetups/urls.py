from django.urls import path
from . import views

# django looks through all the urls.py files looking for the variable "urlpatterns".
# Therefore always name it properly.
# Always add a "/" to the end of the url name because i
urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail')
]
