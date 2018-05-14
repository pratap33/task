from django.conf.urls import url
from userapp.views import Homepage,Loginpage,Showpage
from . import views
app_name='userapp'
urlpatterns=  [
    url(r'^homepage$',Homepage.as_view()),
    url(r'^loginpage$',Loginpage.as_view()),
    url(r'^showpage$',Showpage.as_view()),
]