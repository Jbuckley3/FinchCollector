from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch
from .forms import FinchForm
from django.http import HttpResponse


# Home view


# index view - shows all the cats at '/cats'
def finches_index(request):
    # collect our objects from the database
    # this uses the objects object on the Cat model class
    # the objects object has a method called all
    # all grabs all of the entities using the parent model(in this case, Cat)
    Finches = Finch.objects.all()
    # print(cats)
    # for cat in cats:
    #     print(cat)
    # just like in ejs, we can pass some data to our views
    return render(request, '/Users/joshbuckley/sei/ga-code/django-env/finch-collector/finchcollector/main_app/templates/finches/index.html', { 'Finches': Finches })

# About view
def about(request):
    return render(request, 'about.html')

# Finch list view
class FinchListView(ListView):
    model = Finch
    template_name = 'main_app/finch_list.html'

# Finch detail view
def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, '/Users/joshbuckley/sei/ga-code/django-env/finch-collector/finchcollector/main_app/templates/finches/detail.html', {'finch': finch})

# Finch create view
class FinchCreateView(CreateView):
    model = Finch
    form_class = FinchForm
    template_name = 'main_app/finch_form.html'
    success_url = '/finches/'  # Adjust this URL as needed

# Finch update view
class FinchUpdateView(UpdateView):
    model = Finch
    form_class = FinchForm
    template_name = 'main_app/finch_form.html'
    success_url = '/finches/'  # Adjust this URL as needed

# Finch delete view
class FinchDeleteView(DeleteView):
    model = Finch
    template_name = 'main_app/finch_confirm_delete.html'
    success_url = '/finches/'  # Adjust this URL as needed



def all_finches(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})



# index view - shows all the finches at '/finches'
def all_finches(request):
    # collect finches from the database
    finches = Finch.objects.all()
    # pass the finches data to the template
    return render(request, 'finches/index.html', { 'finches': finches })