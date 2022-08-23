from django.shortcuts import render, get_object_or_404
from . models import Playground

# Create your views here.
def index(request):
    playground = Playground.objects
    return render(request,'index.html',{'playground' :playground })

def details(request, play_id):
    play_detail = get_object_or_404(Playground,pk=play_id)
    return render(request,'detail.html',{'play':play_detail})