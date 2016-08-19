from __future__ import unicode_literals

from django.db import models

COUNTRY_CHOICES = (
    ('US', 'United States'),
    ('AR', 'Argentina'),
    ('ES', 'Spain'),
)


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=2, choices=COUNTRY_CHOICES)

    class Meta:
        abstract = True


class Student(Person):
    scholarship_granted = models.BooleanField(default=False)


class Teacher(Person):
    pass


class CourseClass(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    datetime = models.DateTimeField()

    teacher = models.ForeignKey(Teacher)
    students = models.ManyToManyField(Student)
