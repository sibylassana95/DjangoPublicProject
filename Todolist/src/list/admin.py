from .models import Task
from django.contrib import admin

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Task, TaskAdmin)
