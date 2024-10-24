from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    print(request.GET)
    if request.method=="POST":
        a=int(request.POST.get('snum1'))
        b=int(request.POST.get('snum2'))
        if a>b:
            result=True
        else:
            result=False    
    return render(request,'index.html',{'res':result})