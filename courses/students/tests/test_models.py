from datetime import date, datetime

from django.core.exceptions import ValidationError
from django.test import TestCase

from ..models import Person, Student, Teacher, CourseClass
from . import factories


class StudentModelTestCase(TestCase):

    def test_create_student(self):
        Student.objects.create(
            first_name='John',
            last_name='Doe',
            birth_date=date(1980, 1, 1),
            nationality='US',
            scholarship_granted=True
        )
        self.assertEqual(Student.objects.count(), 1)
        st = Student.objects.first()
        self.assertEqual(st.first_name, 'John')
        self.assertEqual(st.scholarship_granted, True)

    def test_create_student_invalid_field_types(self):
        with self.assertRaises(ValidationError):
            Student.objects.create(
                first_name=1,
                last_name=False,
                birth_date='John',
                nationality=1.0,
                scholarship_granted='Doe'
            )


class TeacherModelTestCase(TestCase):

    def test_create_teacher(self):
        Teacher.objects.create(
            first_name='John',
            last_name='Doe',
            birth_date=date(1980, 1, 1),
            nationality='US',
        )
        self.assertEqual(Teacher.objects.count(), 1)
        te = Teacher.objects.first()
        self.assertEqual(te.first_name, 'John')

    def test_create_teacher_invalid_field_types(self):
        with self.assertRaises(ValidationError):
            Teacher.objects.create(
                first_name=1,
                last_name=False,
                birth_date='John',
                nationality=1.0,
            )


class CourseClassModelTestCase(TestCase):

    def setUp(self):
        self.te = factories.TeacherFactory(first_name='Charlie')
        self.st1 = factories.StudentFactory(first_name='Alan')
        self.st2 = factories.StudentFactory(first_name='Rosie')

    def test_create_courseclass(self):
        cc = CourseClass.objects.create(
            title='Object Oriented Programming',
            description='Learn how to use the OOP paradigm',
            datetime=datetime.now(),
            teacher=self.te,
        )
        cc.students.add(self.st1)
        cc.students.add(self.st2)
        self.assertEqual(CourseClass.objects.count(), 1)
        cc = CourseClass.objects.first()
        self.assertEqual(cc.students.count(), 2)
        self.assertEqual(self.st1.courseclass_set.count(), 1)
        self.assertEqual(self.te.courseclass_set.count(), 1)
        self.assertEqual(cc.teacher, self.te)
