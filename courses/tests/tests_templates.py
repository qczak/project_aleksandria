from django.test import TestCase
from courses import factories
from django.urls import  reverse


class TestTemplateCourseDetail(TestCase):

    def test_template_course_detail_for_logged_in_user(self):
        user = factories.UserFactory()
        course = factories.CourseFactory()
        detail_url = reverse('course-detail', kwargs={ 'pk': course.id })
