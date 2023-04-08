from django.contrib import admin
from todo.models import Todo, TodoList


class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (TodoInline,)



@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'completed', 'favorite')
    list_filter = ('due_date','completed', 'favorite')
    search_fields = ('title', )
