from django.db import models

# Create your models here.


class Usersn(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


class Persons(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)


class Athoor(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    brth_date = models.DateField()


class Users(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)


# class Commints(models.Model):
#     users = models.ManyToManyRel(Users)
#
#
# class Books(models.Model):
#     # Athoor = models.ManyToManyRel(Athoor)
#     commints = models.ManyToManyRel(Commints.users)

