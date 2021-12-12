from django.shortcuts import render
from .models import Contact, Record, Photo,  Nxt_Match, New, Videos, UpComingMatches
from .forms import ContactForm
from django.core import validators
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse

def next_match(request):
    queryset = Nxt_Match.objects.all()
    context = {
        "matches": queryset,
    }
    return render(request, 'club/previous_matches.html', context)

def photo(request):
    queryset = Photo.objects.all()
    context = {
       "photos": queryset,
    }
    return render(request, 'club/gallery.html', context)

def example3(request):
    queryset = Contact.objects.all()
    context = {
       "example3": queryset,
    }
    return render(request, 'club/about.html', context)

def photo3(request):
    queryset = Record.objects.all()
    context = {
       "photos": queryset,
    }
    return render(request, 'club/index.html', context)


def contact(request):
    thank = False
    if request.method=="POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'club/contact.html', {'thank': thank})

def nxt_match(request , sid):
    match = Nxt_Match.objects.filter(id=sid)
    params = {"match": match[0]}
    return render(request, 'club/score_card_view.html', params)

def news_detail(request , sid):
    news_d = New.objects.filter(id=sid)
    return render(request, 'club/news_details.html', {'news_d': news_d[0]})

def new(request):
    queryset = New.objects.all()
    params = {
        "news": queryset,
    }
    return render(request, 'club/news.html', params)


def playerdetail(request, myid):

    # Fetch the product using the id
    record = Record.objects.filter(id=myid)
    return render(request, 'club/players_detail.html', {'record':record[0]})


def innings_divider(request , sid):
    match = Nxt_Match.objects.filter(id=sid)
    params = {"match": match[0]}
        #return render(request, 'shop/score_card_view.html', {'match': match[0]}, sr)
    return render(request, 'club/score_card_view.html', params)

def videos(request):
    queryset = Videos.objects.all()
    context = {
        "videos": queryset,
    }
    return render(request, 'club/videos.html', context)

def upcoming_matches(request):
    queryset = UpComingMatches.objects.all()
    context = {
        "upcoming_matches": queryset,
    }
    return render(request, 'club/upcoming_matches.html', context)