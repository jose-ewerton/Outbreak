from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'
    
class LoginView(TemplateView):
    template_name = 'login.html'
    
class RegisterView(TemplateView):
    template_name = 'register.html'
    
class FeedView(TemplateView):
    template_name = 'feed.html'

class CreateNarrative(CreateView):
    models = ''
    fields = []
    
class ListNarrative(ListView):
    model = ''

class UpdateNarrative(UpdateView):
    model = ''
    fields = []
    #redirecionamento
    success_url = '/'

class DetailNarrative(DetailView):
    models = ''

class DeleteNarrative(DeleteView):
    model = ''
    success_url = '/'


