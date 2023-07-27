from django.shortcuts import render

# Create your views here.
def web(request):
    d = {'name': 'VYSHNAVI', 'age': 18}
    return render(request, 'web.html', context=d)
