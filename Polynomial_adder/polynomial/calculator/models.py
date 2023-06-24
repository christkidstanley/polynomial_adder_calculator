from django.db import models


# Create your models here.
class Equation(models.Model):
    equation_x = models.CharField(max_length=100)
    equation_y = models.CharField(max_length=100)

    def __str__(self):
        return "Equation X:{}".format(self.equation_x) + '\n' + "Equation Y:{}".format(self.equation_y)
