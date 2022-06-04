import datetime

from django.db import models
from django.utils import timezone
from django.utils.timezone import make_aware


class Coupon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(default=make_aware(datetime.datetime.min))
    end_time = models.DateTimeField(default=make_aware(datetime.datetime.max))

    @property
    def is_available(self):
        now = timezone.now()
        return self.start_time < now < self.end_time

    # https://forum.djangoproject.com/t/how-to-filter-model-property-in-views/11869/11
    @classmethod
    def get_available_coupons(cls):
        return [coupon for coupon in cls.objects.all() if coupon.is_available]
