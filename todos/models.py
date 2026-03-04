from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        result = {}
        result["id"] = self.id
        result["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%SZ')
        result["text"] = self.text
        return result
