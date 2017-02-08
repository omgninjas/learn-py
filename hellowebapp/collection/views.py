from django.shortcuts import render

# Create your views here.
def index(request):
    # defining the variable
    num = 6
    thing = 'Thing Name'
    # this is your new view 
    return render(request, 'index.html', {
        'number': num,
        'thing' : thing,
    })