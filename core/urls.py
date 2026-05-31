from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    
    path('classes/', views.classes, name='classes'),

    path(
        "class/<slug:class_slug>/",
        views.class_detail,
        name="class_detail",
    ),

    path(
        "class/<slug:class_slug>/<slug:subject_slug>/",
        views.subject_detail,
        name="subject_detail",
    ),

    path(
        "class/<slug:class_slug>/<slug:subject_slug>/<slug:chapter_slug>/",
        views.chapter_detail,
        name="chapter_detail",
    ),
    
    path(
        "about", views.about, name='about'
    )
]
