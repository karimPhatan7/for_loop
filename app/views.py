from django.shortcuts import render

# Create your views here.
def forloop(request):
    data={'name':'Karim','age':'10'}
    return render(request,'forloop.html',data)