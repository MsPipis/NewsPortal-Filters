from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, UpdateView

from .models import New, Category, NewCategory
from .filters import New_Filter, Search_Filter
from .forms import NewForm
from django.shortcuts import reverse


class NewsList(ListView):
    model = New
    ordering = 'name'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10 # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = New_Filter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = New_Filter (self.request.GET, queryset=self.get_queryset())
        return context


class NewDetail(DetailView):
    model = New
    template_name = 'new.html'
    context_object_name = 'new'

    def get_absolute_url(self):
        return f'/news/'


# Добавляем новое представление для создания товаров.
class NewCreate(CreateView):
    form_class = NewForm
    model = New
    template_name = 'news_create.html'


    def create_new(request):
        form_class = NewForm()

        if request.method == 'POST':
            form_class = NewForm(request.POST)
            if form_class.is_valid():
                form_class.save()
                return HttpResponseRedirect('/news/')
        return render(request, 'news_create.html', {'form':form})


class NewSearch(ListView):
    model = New
    template_name = 'search.html'
    context_object_name = 'news'
    paginate_by = 2


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = Search_Filter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = Search_Filter (self.request.GET, queryset=self.get_queryset())
        return context


class NewDelete(DeleteView):
    model = New
    template_name = 'delete.html'
    success_url = reverse_lazy('news_list')

class NewUpdate(UpdateView):
    form_class = NewForm
    model = New
    template_name = 'news_create.html'