from django.db import models


class Classes(models.Model):
    caption = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ForeignKey('Classes')


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    cls = models.ManyToManyField('Classes')


class Administrator(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)