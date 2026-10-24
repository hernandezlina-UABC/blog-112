from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Render a template and return http respons
# Create your views here.
class HomePageView(TemplateView): # Class Based Views - Inheritance (OOP)
    template_name = "pagesTemplates/home.html"
    
    def get_context_data(self, **kwargs):
        # kwargs is for when you want to...
        context =  super().get_context_data(**kwargs)
        print(context)
        context['name'] = "Jeremy"
        print(context)
        return context
    
class AboutPageView(TemplateView):
    template_name = "pagesTemplates/about.html"
    
    
# Functin Based Views
def contact_page(request):
    # print(request.__dict__)
    # return HttpResponse("Hello World from a FBV")
    contact_info = {
        "name": "Lina",
        "address": "Something 404, NF",
        "email": "lina.hernandez@sdgku.edu"
    }
    
    
    return render(request, "pagesTemplates/contact.html", contact_info)