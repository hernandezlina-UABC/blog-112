from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Create your views here.
class HomePageView(TemplateView): # Class Based Views - Inheritance (OOP)
    template_name = "pagesTemplates/home.html"
    
class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"
    
    
# Functin Based Views
def contact_page(request):
    print(request.__dict__)
    return HttpResponse("Hello World from a FBV")