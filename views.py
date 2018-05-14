from django.shortcuts import render
from  django.views.generic import View
class Homepage(View):
    def get(selfself,request):
        return render(request, 'homepage.html')
class Loginpage(View):
    def get(self,request):
        return render(request, 'loginpage.html')
class Showpage(View):
    def post(self,request):
        return render(request, 'showpage.html')
