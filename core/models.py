from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Subject(models.Model):
    class_level = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.class_level} - {self.name}"


class Chapter(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('note', 'Note'),
        ('pdf', 'PDF'),
        ('video', 'Video'),
    ]

    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    drive_link = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
