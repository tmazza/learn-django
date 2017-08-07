from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('question_text', 'pub_data', 'was_publish_recently')
  fieldsets = [
    (None,          {'fields': ['question_text']}),
    ('Datas',       {'fields': ['pub_data'], 'classes': ['collapse'] }),
  ]
  inlines = [ChoiceInline]
  list_filter = ['pub_data']
  search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
