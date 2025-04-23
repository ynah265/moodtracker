from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import MoodEntry
from django.contrib import messages


class MoodCreateView(LoginRequiredMixin, CreateView):
    ...
    def form_valid(self, form):
        messages.success(self.request, "Mood created successfully!")
        return super().form_valid(form)

class MoodUpdateView(LoginRequiredMixin, UpdateView):
    ...
    def form_valid(self, form):
        messages.success(self.request, "Mood updated successfully.")
        return super().form_valid(form)



class MoodListView(LoginRequiredMixin, ListView):
    model = MoodEntry
    template_name = 'moods/mood_list.html'
    context_object_name = 'mood_list'


class MoodDetailView(LoginRequiredMixin, DetailView):
    model = MoodEntry
    template_name = 'moods/mood_detail.html'


class MoodCreateView(LoginRequiredMixin, CreateView):
    model = MoodEntry
    template_name = 'moods/mood_new.html'
    fields = ['mood', 'journal_entry']
    success_url = reverse_lazy('mood_list')


class MoodUpdateView(LoginRequiredMixin, UpdateView):
    model = MoodEntry
    template_name = 'moods/mood_edit.html'
    fields = ['mood', 'journal_entry']
    success_url = reverse_lazy('mood_list')


class MoodDeleteView(LoginRequiredMixin, DeleteView):
    model = MoodEntry
    template_name = 'moods/mood_delete.html'
    success_url = reverse_lazy('mood_list')
