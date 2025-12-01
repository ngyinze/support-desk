import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support_system.settings')
django.setup()

from tickets.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

# Test data with valid password
data = {
    'username': 'testuser_signup_v2',
    'email': 'test2@example.com',
    'password1': 'TestPassword123!',
    'password2': 'TestPassword123!',
}

form = CustomUserCreationForm(data=data)
if form.is_valid():
    print("Form is valid")
    user = form.save()
    print(f"User created: {user.username} (ID: {user.id})")
else:
    print("Form errors:", form.errors)
