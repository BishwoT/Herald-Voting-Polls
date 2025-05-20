from django.contrib import admin
from .models import HelpRequest

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'submitted_at', 'status')
    list_filter = ('status', 'submitted_at')
    search_fields = ('user__email', 'description')
