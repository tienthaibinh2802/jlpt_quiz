from django.db import models
from ckeditor.fields import RichTextField  # type: ignore

# Test Model: Chứa thông tin các bài kiểm tra
class Test(models.Model):
    title = models.CharField(max_length=200)  # Tên bài kiểm tra
    level = models.CharField(
        max_length=10,
        choices=[('N5', 'N5'), ('N4', 'N4'), ('N3', 'N3'), ('N2', 'N2'), ('N1', 'N1')]  # Cấp độ bài kiểm tra
    )
    category = models.CharField(
        max_length=50,
        choices=[  # Danh mục bài kiểm tra
            ('kanji', 'Kanji'),
            ('tu_vung', 'Từ vựng'),
            ('ngu_phap', 'Ngữ pháp'),
            ('doc_hieu', 'Đọc hiểu'),
            ('nghe_hieu', 'Nghe hiểu'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo bài kiểm tra

    def __str__(self):
        return f"{self.title} ({self.level} - {self.category})"  # Định dạng hiển thị trong Admin


# Câu hỏi: Liên kết với bài kiểm tra (Test)
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')  # Khóa ngoại liên kết với Test
    content = RichTextField()  # Nội dung câu hỏi
    explanation = RichTextField(blank=True)  # Giải thích câu trả lời

    def __str__(self):
        return f"Câu hỏi: {self.content[:50]}"  # Hiển thị phần đầu của nội dung câu hỏi


# Đáp án cho câu hỏi
class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')  # Liên kết với Question
    text = models.CharField(max_length=255)  # Nội dung đáp án
    is_correct = models.BooleanField(default=False)  # Đúng/Sai

    def __str__(self):
        return f"{self.text} ({'Đúng' if self.is_correct else 'Sai'})"  # Hiển thị trạng thái đáp án


# Bình luận người dùng
class Comment(models.Model):
    name = models.CharField(max_length=100)  # Tên người bình luận
    email = models.EmailField(blank=True)  # Email người bình luận
    message = models.TextField()  # Nội dung bình luận
    created_at = models.DateTimeField(auto_now_add=True)  # Thời gian tạo bình luận

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d')}"  # Hiển thị tên và ngày bình luận
