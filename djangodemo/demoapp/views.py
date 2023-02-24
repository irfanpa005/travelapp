from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,MeetTheTeam


# Create your views here.
def demo(request):
    place_datas = Place.objects.all()
    team_members = MeetTheTeam.objects.all()
    return render(request, 'index.html', {'place': place_datas,'team':team_members})
