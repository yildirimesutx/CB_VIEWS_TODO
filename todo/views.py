from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


class Home(TemplateView):
    template_name = 'todo/home.html'

class TodoCreate(CreateView):
    model= Todo 
    form_class = TodoForm 
    template_name = "todo/todo_add.html" 
    success_url = reverse_lazy("list")  

class TodoList(ListView):
     model= Todo
     template_name = 'todo/todo_list.html'
    # context_object_name = 'todos' #-context name istdeğimiz ismi veriyoruz template de karşılarken o isimle kullanılır.bunu yazmazsak default olarak todo_list ile karşılayabiliyoruz 

class TodoUpdate(UpdateView): 
    model = Todo
    form_class = TodoForm
    template_name= "todo/todo_update.html"
    success_url = reverse_lazy("list")


class TodoDelete(DeleteView):
    model = Todo
    
    template_name= "todo/todo_delete.html"
    success_url = reverse_lazy("list")

class TodoDetail(DetailView):
    model= Todo
    # template_name = "todo/todo_detail.html"   docs da belirttilen default isme karşılık geldiği için belirtmedik