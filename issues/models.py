from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Status(models.Model):
    name = models.CharField(max_length=128)
    description =models.CharField(max_length=256)
    

    def __str__(self):
        return self.name
    
class Issue(models.Model):
    name = models.CharField(max_length=128)
    description =models.CharField(max_length=256)
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reporter"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee",
        blank=True, null=True
    )
    create_on = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])