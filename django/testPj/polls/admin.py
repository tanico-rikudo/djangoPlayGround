from django.contrib import admin

# Register your models here.
from .models import Question,Choice

# admin.site.register(Question)
# admin.site.register(Choice)

# class QuestionAdmin(admin.ModelAdmin):
#     fields=['pub_date','question_text']

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets=[
#         (None, {'fields': ['question_text']}),
#         ('Date info' , {'fields': ['pub_date']}),
#         ]

# class ChoiceInline(admin.StackedInline):
#     model=Choice
#     extra=3

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3



class QuestionAdmin(admin.ModelAdmin):
    search_fields=['question_text']#like search
    list_filter=['pub_date']
    list_display=('question_text','pub_date')
    fieldsets=[
        (None, {'fields': ['question_text']}),
        ('Date info' , {'fields': ['pub_date'], 'classes':['collapse']}),
        ]
    inlines=[ChoiceInline]

admin.site.register(Question, QuestionAdmin)
