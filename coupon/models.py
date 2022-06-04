import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import make_aware


class CouponQuerySet(models.QuerySet):
    def available(self):
        return [coupon for coupon in self.all() if coupon.is_available]


class Coupon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(default=make_aware(datetime.datetime.min))
    end_time = models.DateTimeField(default=make_aware(datetime.datetime.max))

    @property
    def is_available(self):
        now = timezone.now()
        return self.start_time < now < self.end_time

    objects = CouponQuerySet.as_manager()
