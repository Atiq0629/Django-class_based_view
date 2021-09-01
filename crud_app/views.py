from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from crud_app import models
from django.urls import reverse_lazy

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'class_based_view/index.html'
    

class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'class_based_view/musician_detail.html'
    
    
class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'class_based_view/musician_form.html'
    

class UpdateMusician(UpdateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician
    template_name = 'class_based_view/update_musician.html'
    
class DeleteMusician(DeleteView):
    context_object_name = 'musician'
    model = models.Musician
    success_url = reverse_lazy('crud_app:index')
    template_name = 'class_based_view/delete_musician.html'
    
    
    
    # template_name = 'class_based_view/index.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['sample1'] = "Sample Text 1"
    #     context['sample2'] = "Sample Text 2"
    #     return context



