from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'home.html')


def Login(request):
    user="sara"
    email="sara@gamil.com"
    context={'username':user,
             'email':email}
    return render(request,'login.html',context)

def Boot(request):
    return render(request,'bootstrap.html')


