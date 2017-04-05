from rest_framework import serializers
from live_sport_app.models import Order

class LiveSportSerializer(serializers.ModelSerializer):
	class Meta:
		model=Order
		fields=['product_name','product_url','price']
