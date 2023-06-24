from django.shortcuts import render, redirect
from .models import Course, Review


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
