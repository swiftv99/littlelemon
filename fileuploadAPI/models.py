from django.db import models
        
        
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='books/pdfs/', max_length=100)
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)