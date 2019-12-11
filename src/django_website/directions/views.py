from django.shortcuts import render

# render 'directions' html page
def directions_view(request):
    return render(request, 'directions/directions.html')