from django.shortcuts import render

# renders 'about webiste' html page
def about_website_view(request):
    return render(request, 'about_website/aboutwebsite.html')
