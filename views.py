from django.shortcuts import render
from django.views.generic import View
from .models import user1
class Homepage(View):
    def get(self,request):
        return render(request, 'homepage.html')
class Loginpage(View):
    def get(self,request):
        return render(request, 'loginpage.html')
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