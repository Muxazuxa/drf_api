from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=20)
    descriprion = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    logo = models.CharField(max_length=1000)


    def __str__(self):
        return self.name

class Contacts(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contacts')
    type = models.CharField(max_length=50)
    value = models.CharField(max_length=50)


    def __str__(self):
        return self.type+' '+self.value

class Branches(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')
    address = models.CharField(max_length=50)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=40)

    def __str__(self):
        return self.address