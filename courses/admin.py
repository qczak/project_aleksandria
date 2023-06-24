from django.contrib import admin
from .models import Course, Enrollment, Review

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'start_data']
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Review)