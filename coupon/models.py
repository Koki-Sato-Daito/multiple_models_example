import datetime
import pytz

from django.db import models

utc = pytz.UTC


class CouponQuerySet(models.QuerySet):
    def available(self):
        return [coupon for coupon in self.all() if coupon.is_available]


class Coupon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(default=datetime.datetime.min)
    end_time = models.DateTimeField(default=datetime.datetime.max)

    @property
    def is_available(self):
        return self.start_time < datetime.datetime.now(tz=utc) < self.end_time

    objects = CouponQuerySet.as_manager()
