from django.shortcuts import render


# render 'home page' html 
def homepage(request):
    return render(request, 'home_page/homepage.html')
