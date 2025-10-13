from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView

from todo.forms import AddTaskForm
from todo.models import Todotask

# user1 vtbPdrvR
class TodoHome(LoginRequiredMixin, ListView):
    template_name = 'todo/index.html'
    context_object_name = 'tasks'
    title_page = 'Главная страница'
    extra_context = {
        'title': 'Главная страница',
    }
    paginate_by = 3

    def get_queryset(self):
        return Todotask.objects.filter(author=self.request.user)


class AddPage(LoginRequiredMixin, CreateView):
    form_class = AddTaskForm
    template_name = 'todo/addpage.html'
    title_page = 'Новая задача'

    def form_valid(self, form):
        w = form.save(commit=False)

        w.author = self.request.user
        return super().form_valid(form)


class ToogleTaskStatus(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Todotask, pk=pk, author=request.user)
        task.status = not task.status
        task.save()
        return redirect('home')

    def get(self, request, pk):
        return redirect('home')


class DeleteTask(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Todotask, pk=pk, author=request.user)
        task.delete()
        return redirect('home')

    def get(self, request, pk):
        return redirect('home')


class AboutView(TemplateView):
    template_name = 'todo/about.html'
    extra_context = {
        'title': 'О сайте',
    }


class ContactView(TemplateView):
    template_name = 'todo/contact.html'
    extra_context = {
        'title': 'Контакты',
    }