from django.contrib import admin
from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # (None,               {'fields': ['question_text']}),
        ("Asked Question",               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
    list_per_page=10
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.list_per_page
    # list_select_related = ('author', 'category')
    ordering = ['pub_date']
    search_fields = ['question_text']
    # fields = ['pub_date', 'question_text']

class ChoiceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['question']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)