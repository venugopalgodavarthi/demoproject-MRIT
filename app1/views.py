from django.shortcuts import render
from django.http import HttpResponse, response
from app1.forms import homeforms,choicedisplay
from app1.models import deptname
import csv

# Create your views here.
def homeviews(request):
    form = homeforms()
    if request.method=='POST':
        form= homeforms(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'home.html',{'form':form})

def displaychoice(request):
    res=False
    users = False 
    if request.method=='POST':
        form= choicedisplay(request.POST)
        res = request.POST['choicedept']
        if res=='IT':
            users=deptname.objects.filter(it=1).order_by('doj')
        elif res=='ELECTRICAL':
            users=deptname.objects.filter(electrical=1).order_by('doj')
        elif res=='MECHANICAL':
            users=deptname.objects.filter(mechanical=1).order_by('doj')
        elif res=='ALL':
            users=deptname.objects.all().order_by('doj')
        elif res=='COMMON':
            users=deptname.objects.filter(mechanical=1,electrical=1,it=1).order_by('doj')
    if request.method=='GET':
        form = choicedisplay()
    return render(request,'display.html',{'form':form,'data':users,'res':res})

def export(request,res1):
    res=res1
    users = False 
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="csv_write.csv"'
    writer = csv.writer(response)
    if res=='IT':
        users=deptname.objects.filter(it=1).order_by('doj')
        response['Content-Disposition']='attachment;filename="csv_it.csv"'
        writer = csv.writer(response)
        writer.writerow(['DEPARTMENT','FACULTYNAME','DOJ'])
        for i in users:
            writer.writerow(['IT',i.facultyname,i.doj])
    elif res=='ELECTRICAL':
        users=deptname.objects.filter(electrical=1).order_by('doj')
        response['Content-Disposition']='attachment;filename="csv_electrical.csv"'
        writer = csv.writer(response)
        writer.writerow(['DEPARTMENT','FACULTYNAME','DOJ'])
        for i in users:
            writer.writerow(['ELECTRICAL',i.facultyname,i.doj])
    elif res=='MECHANICAL':
        users=deptname.objects.filter(mechanical=1).order_by('doj')
        response['Content-Disposition']='attachment;filename="csv_mechanical.csv"'
        writer = csv.writer(response)
        writer.writerow(['DEPARTMENT','FACULTYNAME','DOJ'])
        for i in users:
            writer.writerow(['MECHANICAL',i.facultyname,i.doj])
    elif res=='ALL':
        users=deptname.objects.all().order_by('doj')
        response['Content-Disposition']='attachment;filename="csv_ALL.csv"'
        writer = csv.writer(response)
        writer.writerow(['DEPARTMENT','DEPARTMENT','DEPARTMENT','FACULTYNAME','DOJ',])
        for i in users:
            writer.writerow(['IT','ELECTRICAL','MECHANICAL',i.facultyname,i.doj,])
    elif res=='COMMON':
        users=deptname.objects.filter(mechanical=1,electrical=1,it=1).order_by('doj')
        response['Content-Disposition']='attachment;filename="csv_commonall.csv"'
        writer = csv.writer(response)
        writer.writerow(['DEPARTMENT','DEPARTMENT','DEPARTMENT','FACULTYNAME','DOJ'])
        for i in users:
            writer.writerow(['IT','ELECTRICAL','MECHANICAL',i.facultyname,i.doj,])
    return response



