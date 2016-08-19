from __future__ import unicode_literals

from django.db import models

COUNTRY_CHOICES = (
    # write the list of choices here
)


class Person(models.Model):
    # first_name (char field)
    # last_name (char field)
    # birth_date (date field)
    # nationality (char field with COUNTRY_CHOICES)

    # HINT: Use the class Meta to make this class an abstract Model


class Student(...):
    # scholarship_granted (boolean field)


class Teacher(...):
    # this Model should inherit everything from Person


class CourseClass(models.Model):
    # title (char field)
    # description (text field)
    # datetime (datetime field)
    # teacher (foreign key to Teacher Model)
    # students (many to many relationship to Student model)
