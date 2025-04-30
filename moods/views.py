from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import MoodEntry
from .forms import MoodEntryForm, CustomUserCreationForm



def home(request):
    return render(request, 'moods/home.html')



def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome! You are now signed up and logged in.")
            return redirect('mood_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



class MoodListView(LoginRequiredMixin, ListView):
    model = MoodEntry
    template_name = 'moods/mood_list.html'
    context_object_name = 'mood_list'

    def get_queryset(self):
        return MoodEntry.objects.filter(user=self.request.user).order_by('-date')


class MoodDetailView(LoginRequiredMixin, DetailView):
    model = MoodEntry
    template_name = 'moods/mood_detail.html'


class MoodCreateView(LoginRequiredMixin, CreateView):
    model = MoodEntry
    template_name = 'moods/mood_new.html'
    form_class = MoodEntryForm
    success_url = reverse_lazy('mood_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Mood created successfully!")
        return super().form_valid(form)


class MoodUpdateView(LoginRequiredMixin, UpdateView):
    model = MoodEntry
    template_name = 'moods/mood_edit.html'
    form_class = MoodEntryForm
    success_url = reverse_lazy('mood_list')

    def form_valid(self, form):
        messages.success(self.request, "Mood updated successfully.")
        return super().form_valid(form)


class MoodDeleteView(LoginRequiredMixin, DeleteView):
    model = MoodEntry
    template_name = 'moods/mood_delete.html'
    success_url = reverse_lazy('mood_list')
