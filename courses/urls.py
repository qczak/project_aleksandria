

from django.urls import path
from django.views.generic import TemplateView

import courses
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="courses/base.html"), name="home"),
    path('courses/', views.course_list, name='course-list'),
    path('courses/<int:pk>/', views.course_detail, name='course-detail'),
    path('courses/<int:pk>/add-review', views.add_review, name='add-review'),

]