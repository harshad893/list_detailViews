from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView
from app.models import *
class Home(View):
    def get(self,request):
        return render(request,'app/home.html')

class SchoolListView(ListView):
    model=School
    context_object_name='schools'

class SchoolDetailView(DetailView):
    model=School
    context_object_name='school'

class SchoolCreateView(CreateView):
    model=School
    fields='__all__'

class SchoolUpdateView(UpdateView):
    model=School
    fields='__all__'
