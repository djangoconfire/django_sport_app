from live_sport_app.models import Order
from serializers import LiveSportSerializer
from rest_framework import generics
from rest_framework import permissions

# order_list
class OrderList(generics.ListCreateAPIView):
    queryset =Order.objects.all()
    serializer_class =LiveSportSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
