from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    courseNumber = models.IntegerField(default=0)  # had to add the parameter to make it work
    instructorName = models.CharField(max_length=50)
    duration = models.DecimalField(decimal_places=1, max_digits=3)  # mandatory parameters for DecimalField?

    objects = models.Manager()              # this is the object manager which will help us communicate w/ the database

    def __str__(self):                      # this line of code should display the title of the object
        return self.title + ' ' + str(self.courseNumber)

