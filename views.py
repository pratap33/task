from django.shortcuts import render
from django.views.generic import View
from .models import user1
class Homepage(View):
    def get(self,request):
        return render(request, 'homepage.html')
class Loginpage(View):
    def get(self,request):
        return render(request, 'loginpage.html')
class Loginpage1(View):
    def get(self,request):
        return render(request, 'loginpage1.html')
class Showpage(View):
    def post(self,request):
        return render(request, 'showpage.html')
def insert(request):
    try:
         u1=request.GET['t1']
         p1=int(request.GET['t2'])
         rec=user1.objects.filter(filter(uname='u1').filter(pwrd='p1'))
         return render(request,'showpage.html',{'records':rec})
    except ValueError:
        return render(request, 'errorpage.html')
def function(request):
    try:
         u1=request.GET['t1']
         p1=int(request.GET['t2'])
         rec=user1.objects.filter(filter(uname='u1').filter(pwrd='p1'))
         return render(request,'showpage1.html',{'records':rec})
    except ValueError:
        return render(request, 'errorpage.html')
def split(request):
    try:
        sname = request.POST['t3']
        sbal = int(request.POST['t4'])
        fnum = int(request.POST['t5'])
        a1=rec.actbal
        if (a1>sbal):
            a1=a1-sbal
            user1()
        else:
            return render(request, 'errorpage1.html')

















