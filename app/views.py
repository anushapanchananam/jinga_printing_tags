from django.shortcuts import render

# Create your views here.
def web(request):
    d = {'name': 'VYSHNAVI', 'age': 18}
    return render(request, 'web.html', context=d)



def condition1(request):
    c = {'a':100, 'b':200,'c':500}
    return render(request,'condition1.html', context=c)