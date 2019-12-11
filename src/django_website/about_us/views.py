from django.shortcuts import render

# renders 'about us' html page
def about_us(request):
    return render(request, 'about_us/about.html')