from django.test import TestCase
from django.urls import reverse
from .models import CustomUser, Ticket

class TicketTests(TestCase):
    def setUp(self):
        self.customer = CustomUser.objects.create_user(username='customer', password='password', is_customer=True)
        self.staff = CustomUser.objects.create_user(username='staff', password='password', is_support_staff=True)
        self.ticket = Ticket.objects.create(title='Test Ticket', description='Test Description', created_by=self.customer)

    def test_ticket_creation(self):
        self.assertEqual(self.ticket.title, 'Test Ticket')
        self.assertEqual(self.ticket.status, 'Pending')

    def test_customer_dashboard(self):
        self.client.login(username='customer', password='password')
        response = self.client.get(reverse('ticket_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Ticket')

    def test_staff_dashboard(self):
        self.client.login(username='staff', password='password')
        response = self.client.get(reverse('ticket_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Ticket')

    def test_ticket_detail_access(self):
        self.client.login(username='customer', password='password')
        response = self.client.get(reverse('ticket_detail', args=[self.ticket.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Description')
