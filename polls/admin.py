from django.contrib import admin

from polls.models import Question, Choice

# class ChoiceInline(admin.StackedInline): # question에서 바로 요소 추가 탭
#     model = Choice
#     extra = 0
class ChoiceInline(admin.TabularInline): # question에서 바로 요소 추가 탭
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


