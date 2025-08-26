from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    published_year = models.DateField()  # hoặc IntegerField nếu chỉ lưu năm

    def __str__(self):
        return self.title