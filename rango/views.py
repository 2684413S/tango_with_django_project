from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category


#this function is reponsible for the main view.
def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    
    #return HttpResponse("Rango says hey there partner!" + " hyperlink to about")
    context_dict = {}
    context_dict["boldmessage"] = "Crunchy, creamy, cookie, candy, cupcake!"
    context_dict["categories"] = category_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page." + " hyperlink to index") 


