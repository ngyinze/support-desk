from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Ticket, Comment

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'priority')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a reply...'}),
        }

class TicketStatusForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('status', 'priority')

