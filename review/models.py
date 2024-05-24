from django.db import models

class Chorus(models.Model):
    #名前
    yourname = models.CharField(max_length=50)
    #曲名
    songname = models.CharField(max_length=50)
    #担当パート
    part = models.CharField(max_length=20)
    #練習の振り返り
    review = models.TextField()
    #作成日、更新日時
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.yourname} 曲名: {self.songname} 作成日: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"