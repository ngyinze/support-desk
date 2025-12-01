from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Ticket, Comment

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_customer', 'is_support_staff', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('is_customer', 'is_support_staff')}),
    )

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'created_by', 'assigned_to', 'created_at')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description', 'created_by__username')
    inlines = [CommentInline]

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment)
