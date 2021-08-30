from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'home3.html')
def blogs(request):
    return render(request,'blog.html')
def college(request):
    return render(request,'college.html')
def student(request):
    return render(request,'student.html')
def online(request):
    return render(request,'online.html')
def Apply(request):
    return render(request,'Admission1.html')
def registration(request):
    return render(request,'a1.html')
def About(request):
    return render(request,'About.html')