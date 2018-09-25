from django.db import models

class Email(models.Model):
	From = models.EmailField(max_length=254)
	To = models.EmailField(max_length=254)
	Subject = models.CharField(max_length=350)
	Date = models.CharField(max_length=60)
	Body = models.TextField(max_length=100000)
	Raw = models.TextField(max_length=200000)

	def __str__(self):
		return self.Subject