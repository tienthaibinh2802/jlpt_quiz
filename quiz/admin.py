from django.contrib import admin
from .models import Test, Question, AnswerOption


class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 4  # Luôn hiển thị sẵn 4 dòng để nhập (A, B, C, D)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'question_count', 'level', 'category')
    search_fields = ('title',)
    list_filter = ('level', 'category')

    def question_count(self, obj):
        return obj.questions.count()

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('short_content', 'test', 'get_level', 'get_category')
    search_fields = ('content',)
    # ✅ Thêm lọc theo Test nữa
    list_filter = ('test', 'test__level', 'test__category')
    list_per_page = 30  # 30 câu hỏi 1 trang

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
