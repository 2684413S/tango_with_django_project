from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from django.shortcuts import redirect


#this function is reponsible for the main view.
def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    
    #return HttpResponse("Rango says hey there partner!" + "<a href='/rango/about/'About</a>")
    context_dict = {}
    context_dict["boldmessage"] = "Crunchy, creamy, cookie, candy, cupcake!"
    context_dict["categories"] = category_list
    context_dict["pages"] = pages_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {}
    context_dict["boldmessage"] = "This tutorial has been put together by Ayleen Sohaib."
    return render(request, 'rango/about.html', context=context_dict) 

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render (request, 'rango/category.html', context=context_dict)

#for handling forms
def add_category(request):
    #create category form
    form = CategoryForm()

    #check if HTTP request was a Post
    if request.method == 'POST':
        form = CategoryForm(request.POST)

    #saves form data provided by user to the model, redirects to Rango homepage 
    if form.is_valid():
        form.save(commit=True)
        return redirect('/rango/')

    else:
        #redisplay form with error messages if there are errors.
        print(form.errors)
    
    return render(request, 'rango/add_category.html', {'form': form})