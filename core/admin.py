from django.contrib import admin
from .models import About, Project, Message, Pricing

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated')
    readonly_fields = ('updated',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    list_filter = ('created',)
    search_fields = ('name', 'description')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created', 'is_read')
    list_filter = ('is_read', 'created')
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'initial_price', 'monthly_maintenance')
    list_editable = ('initial_price', 'monthly_maintenance')