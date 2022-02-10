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

def Test(request):
    return render(request,'test.html')

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
