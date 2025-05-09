from django.db import models
from ckeditor.fields import RichTextField # type: ignore

class Test(models.Model):
    title = models.CharField(max_length=200)
    level = models.CharField(max_length=10, choices=[('N5', 'N5'), ('N4', 'N4'), ('N3', 'N3'), ('N2', 'N2'), ('N1', 'N1')])
    category = models.CharField(max_length=50, choices=[
        ('kanji', 'Kanji'),
        ('tu_vung', 'Từ vựng'),
        ('ngu_phap', 'Ngữ pháp'),
        ('doc_hieu', 'Đọc hiểu'),
        ('nghe_hieu', 'Nghe hiểu'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.level} - {self.category})"


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    content = RichTextField()
    explanation = RichTextField(blank=True)

    def __str__(self):
        return f"Câu hỏi: {self.content[:50]}"


class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Đúng' if self.is_correct else 'Sai'})"
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"