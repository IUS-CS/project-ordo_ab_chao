from django.shortcuts import render

# Create your views here.
def about_website_view(request):
    return render(request, 'about_website/aboutwebsite.html')
