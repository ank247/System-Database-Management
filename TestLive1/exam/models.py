
from django.db import models

class paper(models.Model):
      type=models.CharField(max_length=20)
      time=models.DateTimeField()
      duration=models.DecimalField(max_digits=3,decimal_places=2)
      file=models.FileField()

      def __str__(self):
          return self.type

