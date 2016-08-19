# Build your first data model

In this assignment we will take a first look at how to create Django Models.

We will create a basic data model for a Course system. It will handle three different types of data: Information about Students, Teachers and course classes. There will also be relationships between these three classes. A course class will have many students, and only one teacher. But one student can also participate in many course classes, which builds a `ManyToMany` relationship between `Student` and `CourseClass`.

You will notice in the `students/models.py` module, that we have specified the list of fields and field types for each of the models. You will just need to write what's required for each field using the Django Model Fields syntax.

The `Person` class is an "abstract" Model. Which means that no instances are supposed to be created from that class. It's just built for other Models to inherit from it. That's why you won't need to repeat all similar fields in `Student` and `Teacher` models, because both of them should inherit from `Person`.

Once you set up your models, make sure to create the proper database `Migration`. For that you will need to use the built-in Django `makemigrations` command.
