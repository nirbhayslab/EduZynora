from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Class, Subject, Chapter

def home(request):
    classes = Class.objects.all()
    return render(request, "core/home.html", {"classes": classes})

def class_detail(request, class_slug):
    class_obj = get_object_or_404(Class, slug=class_slug)
    subjects = class_obj.subjects.all()

    return render(
        request,
        "core/class_detail.html",
        {"class": class_obj, "subjects": subjects},
    )

def subject_detail(request, class_slug, subject_slug):
    class_obj = get_object_or_404(Class, slug=class_slug)
    subject = get_object_or_404(
        Subject, slug=subject_slug, class_level=class_obj
    )
    chapters = subject.chapters.all()

    return render(
        request,
        "core/subject_detail.html",
        {
            "class": class_obj,
            "subject": subject,
            "chapters": chapters,
        },
    )

def chapter_detail(request, class_slug, subject_slug, chapter_slug):
    class_obj = get_object_or_404(Class, slug=class_slug)
    subject = get_object_or_404(
        Subject, slug=subject_slug, class_level=class_obj
    )
    chapter = get_object_or_404(
        Chapter, slug=chapter_slug, subject=subject
    )

    resources = resources = {
    "notes": chapter.resources.filter(resource_type="notes"),
    "examples": chapter.resources.filter(resource_type="example"),
    "exercises": chapter.resources.filter(resource_type="exercise"),
    "pdfs": chapter.resources.filter(resource_type="pdf"),
    "videos": chapter.resources.filter(resource_type="video"),
}

    return render(
        request,
        "core/chapter_detail.html",
        {
            "class": class_obj,
            "subject": subject,
            "chapter": chapter,
            "resources": resources,
        },
    )
