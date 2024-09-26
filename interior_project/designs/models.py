from django.db import models

class Design(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='design_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class Favorite(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE)

    def __str__(self):
        return f"Favorite - {self.design.title }"
