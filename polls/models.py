from django.db import models

# Create your models here.
# 모델이라는 특성을 상속 받은 클래스 생성
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 문자열로 변환해주는 함수
    def __str__(self):
        return self.question_text

class Choice(models.Model): # 문항
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # foreignKey Question과 연결
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



