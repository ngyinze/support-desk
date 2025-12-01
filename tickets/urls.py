from django.urls import path
from .views import SignUpView, TicketListView, TicketCreateView, TicketDetailView

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('tickets/', TicketListView.as_view(), name='ticket_list'),
    path('tickets/create/', TicketCreateView.as_view(), name='create_ticket'),
    path('tickets/<int:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('', TicketListView.as_view(), name='home'),
]
