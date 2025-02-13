from django.shortcuts import render
from .models import *
# Create your views here.

def meet_our_team(request):
	team = MeetOurTeam.objects.all()

	context = {
	  'team': team
	}
	return render(request, 'store/meet_our_team.html', context)