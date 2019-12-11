from django.shortcuts import render

# render 'contact us' html page
def contact_page(request):
    return render(request, 'contact_us/contact.html')