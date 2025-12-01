# Support Ticketing System

A Django-based support ticketing system where customers can raise issues and staff can manage them.

## Features
- **User Roles**: Distinct Customer and Support Staff roles.
- **Ticket Management**: Create, view, and track tickets.
- **Conversation**: Forum-style comments on tickets.
- **Staff Tools**: Update ticket status and priority.
- **Dashboard**: Filtered views for Customers (own tickets) and Staff (all tickets).
- **Admin Panel**: Customized admin interface for managing users and tickets.

## Setup Instructions

1.  **Clone the repository** (or navigate to the project directory).
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate  # Windows
    # source venv/bin/activate  # Linux/Mac
    ```
3.  **Install dependencies**:
    ```bash
    pip install django
    ```
4.  **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
5.  **Create a Superuser (Staff)**:
    ```bash
    python manage.py createsuperuser
    ```
6.  **Run the server**:
    ```bash
    python manage.py runserver
    ```

## Usage

### Customer
1.  Sign up for an account.
2.  Log in to access the Dashboard.
3.  Click "+ New Ticket" to raise an issue.
4.  View ticket details and reply to staff comments.

### Support Staff
1.  Log in with a staff account (or superuser).
2.  View all tickets on the Dashboard.
3.  Open a ticket to reply or update its Status/Priority.
4.  Use the Admin Panel (`/admin/`) for advanced management.

## Project Structure
- `support_system/`: Project settings and configuration.
- `tickets/`: Main app containing models, views, and forms.
- `templates/`: HTML templates.
- `static/`: CSS and other static files.
