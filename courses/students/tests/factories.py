from datetime import date

import factory

from .. import models


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Student

    first_name = 'John'
    last_name = 'Doe'
    birth_date = date(1987, 1, 1)
    nationality = 'US'


class TeacherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Teacher

    first_name = 'Charlie'
    last_name = 'Scott'
    birth_date = date(1962, 2, 3)
    nationality = 'AR'
