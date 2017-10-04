from django.test import TestCase
from .models import Course, Step
from django.utils import timezone
from django.core.urlresolvers import reverse

class CourseModelTests(TestCase):
    # A test that creates a course w/ the right date
    def test_course_creation(self):
        # Instantiate a course w/ required info
        course = Course.objects.create(
            title="Python Regex",
            description="Learn to write regexes",
        )
        # Declare a 'now' time
        now = timezone.now()
        # Test that the course created_at time is just
        # slightly less than 'now'
        self.assertLess(course.created_at, now)



class StepModelTests(TestCase):
    # Test for successful step creation

    def setUp(self):
        self.course = Course.objects.create(
            title="Fake course 1",
            description="Fake description 1"
        )

    def test_step_creation(self):
        step=Step.objects.create(
            title="Step title",
            description="Step description",
            course=self.course
        )
        self.assertIn(step, self.course.step_set.all())


class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title="Python Testing",
            description="Sample description"
        )
        self.course2 = Course.objects.create(
            title="New Course",
            description="New course description"
        )
        self.step = Step.objects.create(
            title="Intro to Doctests",
            description="Learn to write tests in your docstrings",
            course=self.course
        )


    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])







