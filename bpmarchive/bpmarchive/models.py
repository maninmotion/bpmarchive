__author__ = 'Kevin'
from django.db import models


class Test(models.Model):
    test_text = models.CharField(max_length=200)

    def __unicode__(self):
        return self.test_text
