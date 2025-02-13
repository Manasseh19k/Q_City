from django.urls import path
from . import views

urlpatterns = [
	path('meet_our_team/', views.meet_our_team, name="meet_our_team"),
]