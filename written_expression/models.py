from django.db import models

class WrittenExpressionCorrectAns(models.Model):
    
    def __str__(self):
        return self.answer
        
    answer = models.CharField(max_length = 1)

class WrittenExpressionAns(models.Model):
    
    def __str__(self):
        return f"{self.a}__{self.b}__{self.c}__{self.d}"
    
    A = models.TextField()
    B = models.TextField()
    C = models.TextField()
    D = models.TextField()
    correct = models.ForeignKey(WrittenExpressionCorrectAns, on_delete=models.CASCADE)

class WrittenExpressionQuestions(models.Model):
    
    def __str__(self):
        return self.question

    question = models.TextField()
    answers = models.ForeignKey(WrittenExpressionAns, on_delete=models.CASCADE)