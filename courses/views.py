from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Course, Review, Enrollment


def course_list(request):
    return render(request, 'courses/course_list.html', {"courses": Course.objects.all()})

def course_detail(request, pk):
    return render(
        request,
        'courses/course_detail.html',
        {"course": Course.objects.get(id=pk), "reviews": Review.objects.all()}
    )

def add_review(request, pk):
    course = Course.objects.get(id=pk)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        user = request.user

        review = Review.objects.create(
            course=course,
            user=user,
            rating=rating,
            comment=comment
        )
        return redirect('course-detail', pk=pk)

def add_enroll(request, pk): # /courses/<int:pk>/enroll/
    course = Course.objects.get(id=pk)
    enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
    if created:
        messages.success(request, 'You have successfully enrolled in the course.')
    else:
        messages.error(request, 'You are already enrolled in the course.')
    return redirect('course-detail', pk=pk)