from django.shortcuts import render

# Create your views here.

def things_view(request):
    return render(request, "things/index.html")
