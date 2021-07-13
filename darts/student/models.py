from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.IntegerField(db_column='role_number', primary_key=True)
    name = models.CharField(db_column='name', max_length=500)
    address = models.TextField(db_column='addrress')


class Subject(models.Model):
    id = models.IntegerField(db_column='sub_id', primary_key=True)
    name = models.CharField(db_column='subject_name', max_length=200)


class Marks(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, models.DO_NOTHING)
    subject = models.ForeignKey(Subject, models.DO_NOTHING)
    marks = models.FloatField(db_column='marks')
