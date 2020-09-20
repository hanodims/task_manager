from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
	title = models.CharField(max_length=150)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="boards")

	def __str__(self):
		return self.title


class Task(models.Model):
	board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="tasks")
	description = models.TextField()
	creation_date = models.DateField(auto_now_add=True)
	is_hidden = models.BooleanField()
	is_done = models.BooleanField()

	def __str__(self):
		return self.description
