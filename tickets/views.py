from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormMixin
from .models import Ticket, Comment
from .forms import CustomUserCreationForm, TicketForm, CommentForm, TicketStatusForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class TicketListView(LoginRequiredMixin, ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_support_staff or self.request.user.is_superuser:
            return queryset
        return queryset.filter(created_by=self.request.user)

class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('ticket_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TicketDetailView(LoginRequiredMixin, FormMixin, DetailView):
    model = Ticket
    template_name = 'tickets/ticket_detail.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('ticket_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        if self.request.user.is_support_staff or self.request.user.is_superuser:
            context['status_form'] = TicketStatusForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        # Handle Status Update (Staff only)
        if 'status_update' in request.POST and (request.user.is_support_staff or request.user.is_superuser):
            status_form = TicketStatusForm(request.POST, instance=self.object)
            if status_form.is_valid():
                status_form.save()
                return redirect(self.get_success_url())

        # Handle Comment
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.ticket = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)
