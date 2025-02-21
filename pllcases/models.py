from django.db import models


class PLL_Cases(models.Model):
    id = models.AutoField(primary_key=True)
    cases = models.CharField(max_length=3)
    algorithm = models.CharField(max_length=100)
    setup = models.CharField(max_length=100)
