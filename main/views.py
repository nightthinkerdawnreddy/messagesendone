from django.shortcuts import render
from .models import Mainmodule

# Create your views here.
def home(request):
    if request.method=='POST':
        print(request.POST)
        valuesfrom = request.POST
        namef=valuesfrom['name']
        emailf=valuesfrom['email']
        taskf=valuesfrom['task']
        yearf=valuesfrom['year']
        monthf=valuesfrom['month']
        dayf=valuesfrom['day']
        hourf=valuesfrom['hour']
        minutef=valuesfrom['minute']
        print(len(monthf))
        if len(monthf)==1:
            print("yes it is working")
            monthf="0"+monthf
        if len(dayf)==1:
            dayf="0"+dayf
        if len(hourf)==1:
            hourf="0"+hourf
        if len(minutef)==1:
            minutef="0"+minutef
        datetime=yearf+monthf+dayf+hourf+minutef
        p=Mainmodule(name=namef,email=emailf,task=taskf,tasktime=datetime)
        p.save()
        print(Mainmodule.objects.all())
    return render(request,"home.html")
