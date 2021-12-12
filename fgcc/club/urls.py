
from django.urls import path
from . import views



urlpatterns = [
    path("", views.photo3, name="ClubHome"),
    path("about/", views.example3, name="example3"),
    path("nxt_matchs/<int:sid>", views.innings_divider, name="nxt_match"),
    path("contact/", views.contact, name="ContactUs"),
    path("records/<int:myid>", views.playerdetail, name=""),
    path("matches/", views.next_match, name="Matches"),
    path("gallery/", views.photo, name="photo"),
    path("news/", views.new, name="new"),
    path("news_details/<int:sid>", views.news_detail, name="news_detail"),
    path("videos/",views.videos, name="Videos"),
    path("upcoming_matches/",views.upcoming_matches, name="Up-Coming Matches")


]


