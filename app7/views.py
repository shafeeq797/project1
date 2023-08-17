from django.shortcuts import render,redirect
from app7.models import tbl_cricket,tbl_football
def index(request):
    return render(request,'index.html')
def cricket1(request):
    return render(request,'cricket.html')
def cricket2(request):
    a=tbl_cricket()
    a.player_name=request.POST.get('nme')
    a.age=request.POST.get('age')
    a.player_position=request.POST.get('pp')
    a.place=request.POST.get('plc')
    a.save()
    return redirect('/cricket/')

def football(request):
    return render(request,'football.html')
def football1(request):
    b=tbl_football()
    b.player_name=request.POST.get('nme')
    b.age=request.POST.get('age')
    b.player_position=request.POST.get('pp')
    b.place=request.POST.get('plc')
    b.save()
    return render(request,'footballadded.html')



# Create your views here.
