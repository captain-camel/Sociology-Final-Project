from django.db import models

class Question(models.Model):
    text = models.TextField()
    author = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=10)

    def author_formatted(self):
        if self.author == '':
            return "Anonymous"
        else:
            return self.author

    def author_first_char(self):
        try:
            return self.author[0]
        except IndexError:
            return '?'

    def date_formatted(self):
        return self.date.strftime('%Y-%m-%d %H:%M')

    def __string__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
    
    def __string__(self):
        return self.text

class Resource(models.Model):
    name = models.TextField()
    description = models.TextField()
    link = models.URLField()