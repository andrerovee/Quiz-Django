from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    CATEGORY_CHOICES = [
        ('Art and Literature', 'Arte e letteratura'),
        ('history', 'Storia'),
        ('science', 'Scienze'),
        ('curiosity', "Curiosità"),
        ('sport', "Sport")
    ]

    # Aggiungere il metodo __str__ per rappresentare la categoria
    def __str__(self):
        return self.name

    text = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)


class Question(models.Model):
    text = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text
