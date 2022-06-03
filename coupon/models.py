import datetime

from django.db import models


class Coupon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(default=datetime.datetime.min)
    end_time = models.DateTimeField(default=datetime.datetime.max)

    @property
    def is_available(self):
        return self.start_date < datetime.datetime.now() < self.end_date
