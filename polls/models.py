import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  pub_data = models.DateTimeField('Data de publicação')

  def __str__(self):
    return self.question_text

  def was_publish_recently(self):
    return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

  was_publish_recently.admin_order_field = 'pub_data'
  was_publish_recently.boolean = True
  was_publish_recently.short_description = 'on the top \\o/'

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
