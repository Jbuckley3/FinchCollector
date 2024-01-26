from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Toy
from .forms import FeedingForm
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# index view - shows all the finches at '/finches'
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

# Finch list view
class FinchListView(ListView):
    model = Finch
    template_name = 'main_app/finch_list.html'

# Finch detail view
class FinchDetailView(DetailView):
    model = Finch
    template_name = 'finches/detail.html'

# Finch create view
class FinchCreateView(CreateView):
    model = Finch
    fields = ['name', 'color', 'size']
    template_name = 'main_app/finch_form.html'
    success_url = '/finches/'  # Adjust this URL as needed

# Finch update view
class FinchUpdateView(UpdateView):
    model = Finch
    fields = ['name', 'color', 'size']
    template_name = 'main_app/finch_form.html'
    success_url = '/finches/'  # Adjust this URL as needed

# Finch delete view
class FinchDeleteView(DeleteView):
    model = Finch
    template_name = 'main_app/finch_confirm_delete.html'
    success_url = '/finches/'  # Adjust this URL as needed

# Add this new view for adding a feeding to a finch
def add_finch_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finch_detail', finch_id=finch_id)

# Toy views
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'
