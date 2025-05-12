from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Question, Test, AnswerOption

class QuestionResource(resources.ModelResource):
    test = fields.Field(
        column_name='test',
        attribute='test',
        widget=ForeignKeyWidget(Test, field='title')
    )

    option_a = fields.Field(column_name='option_a')
    option_b = fields.Field(column_name='option_b')
    option_c = fields.Field(column_name='option_c')
    option_d = fields.Field(column_name='option_d')
    correct_option = fields.Field(column_name='correct_option')

    class Meta:
        model = Question
        fields = ('id', 'test', 'content', 'explanation',
                  'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')

    def after_import_row(self, row, row_result, **kwargs):
        question = Question.objects.filter(content=row['content']).last()
        if question:
            # ✅ Xóa đáp án cũ
            question.options.all().delete()

            # ✅ Tạo mới 4 đáp án
            options = {
                'A': row.get('option_a'),
                'B': row.get('option_b'),
                'C': row.get('option_c'),
                'D': row.get('option_d'),
            }
            correct = row.get('correct_option', '').strip().upper()

            for key, text in options.items():
                AnswerOption.objects.create(
                    question=question,
                    text=text,
                    is_correct=(key == correct)
                )
