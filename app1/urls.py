from django.urls import path
from app1 import views
app_name = 'app1'
urlpatterns=[
    path('home/',views.homeviews,name='home'),
    path('display/',views.displaychoice,name='display'),
    path('export/<res1>/',views.export,name='export'),
]