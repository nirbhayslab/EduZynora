from django.db import models
from django.core.exceptions import ValidationError


class Class(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    class_level = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="subjects")

    class Meta:
        unique_together = ("slug", "class_level")

    def __str__(self):
        return f"{self.name} ({self.class_level})"

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="chapters")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        unique_together = ("slug", "subject")

    def __str__(self):
        return self.name



class Resource(models.Model):
    RESOURCE_TYPES = [
        ("notes", "Notes"),
        ("example", "Example"),
        ("exercise", "Exercise"),
        ("pdf", "PDF"),
        ("video", "Video"),
    ]

    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to="resources/", blank=True, null=True)
    external_link = models.URLField(blank=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="resources")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
    
    def clean(self):
        filled = sum(
            bool(field)
            for field in [self.content, self.file, self.external_link]
        )

        if filled != 1:
            raise ValidationError(
                "Exactly one of content, file, or external_link must be provided."
            )
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)



    def __str__(self):
        return self.title

