from django.contrib import admin
from .models import Test, Question, AnswerOption, Comment
from import_export.admin import ImportExportModelAdmin # type: ignore
from .resources import QuestionResource  # ✅ Dùng Resource chuẩn từ resources.py

class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 4

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'question_count', 'level', 'category')
    search_fields = ('title',)
    list_filter = ('level', 'category')

    def question_count(self, obj):
        return obj.questions.count()

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin):  # ✅ Dùng import-export
    resource_class = QuestionResource  # ✅ Kết nối resource
    list_display = ('short_content', 'test', 'get_level', 'get_category')
    search_fields = ('content',)
    list_filter = ('test', 'test__level', 'test__category')
    list_per_page = 30
    inlines = [AnswerOptionInline]

    def short_content(self, obj):
        return obj.content[:50] + "..."

    def get_level(self, obj):
        return obj.test.level
    get_level.short_description = 'Level'

    def get_category(self, obj):
        return obj.test.category
    get_category.short_description = 'Category'

@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'is_correct')
    list_filter = ('is_correct',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'created_at')
    search_fields = ('name', 'message')
    list_filter = ('created_at',)
8