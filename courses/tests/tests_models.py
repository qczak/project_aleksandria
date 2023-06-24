from django.test import TestCase

from courses import factories
from courses.models import Course, Review, Enrollment
from django.contrib.auth.models import User
from datetime import date


''' Testy  bez factory
class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.course = Course.objects.create(
            title="Python",
            description="Python course",
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 10),
            author=self.user,
            price=100.00
        )
class TestCourseModel(BaseTest):

    def test_course_model_str_method(self):
        self.assertEqual(str(self.course), "Python")

class TestEnrollmentModel(BaseTest):

    def setUp(self):
        super().setUp()
        self.enrollment = Enrollment.objects.create(
            user=self.user,
            course=self.course,
        )
    def test_enrolment_model_str_method(self):
        self.assertEqual(str(self.enrollment), "testuser Python")

class TestReviewModel(BaseTest):

    def setUp(self):
        super().setUp()
        self.review = Review.objects.create(
            user=self.user,
            course=self.course,
            rating='1'
        )
    def test_review_model_str_method(self):
        self.assertEqual(str(self.review), "testuser - Python - 1")

'''

'''
class TestCourseModel(TestCase):

    def SetUp(self):
        self.course = factories.CourseFactory()

    def test_course_model_str_method(self):
        self.assertEqual(str(self.course), "Python")

class TestEnrollmentModel(TestCase):

    def setUp(self):
        self.enrollment = factories.EnrollmentFactory()
    def test_enrolment_model_str_method(self):
        self.assertEqual(str(self.enrollment), "testuser Python")

class TestReviewModel(TestCase):
    def SetUp(self):
        self.review = factories.ReviewFactory()
    def test_review_model_str_method(self):
        self.assertEqual(str(self.review), "testuser - Python - 1")

'''



class TestCourseModel(TestCase):

    def setUp(self):
        self.course = factories.CourseFactory(title="Python")
    def test_course_model_str_method(self):
        self.assertEqual(str(self.course), "Python")


class TestReviewModel(TestCase):

    def setUp(self):
        self.review = factories.ReviewFactory()

    def test_review_model_str_method(self):
        expected_str = f"{self.review.user.username} - {self.review.course.title} - {self.review.rating}"
        self.assertEqual(str(self.review), expected_str)


class TestEnrollmentModel(TestCase):
    def setUp(self):

        self.enrollment = factories.EnrollmentFactory()

    def test_enrollment_model_str_method(self):
        expected_str = f"{self.enrollment.user.username} {self.enrollment.course.title}"
        self.assertEqual(str(self.enrollment), expected_str)
