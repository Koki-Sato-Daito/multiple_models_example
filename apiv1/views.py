from drf_multiple_model.views import ObjectMultipleModelAPIView

from coupon.models import Coupon
from item.models import Item
from apiv1.serializers import CouponSerializer, ItemSerializer


class ItemListAPIView(ObjectMultipleModelAPIView):
    # 商品の一覧と
    # 利用できるクーポン一覧
    querylist = [
        {
            'queryset': Item.objects.all(),
            'serializer_class': ItemSerializer,
            'label': 'items',
        },
        {
            'queryset': Coupon.objects.available(),
            'serializer_class': CouponSerializer,
            'label': 'coupons'
        },
    ]

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
