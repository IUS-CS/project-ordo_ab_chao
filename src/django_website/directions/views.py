from django.shortcuts import render

# Create your views here.
def directions_view(request):
    return render(request, 'directions/directions.html')