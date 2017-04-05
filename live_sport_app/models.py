from django.db import models
from user_profile.models import UserProfile


class Order(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Cancelled', 'Cancelled')
    )
    user                = models.ForeignKey(UserProfile,null=True)
    order_id            = models.CharField(max_length=200,null=True)
    product_name        = models.CharField(max_length=200, null=True)
    order_status        = models.CharField(max_length=10, choices=ORDER_STATUS,  null=True,blank=True,)
    product_url         = models.CharField(max_length=100, null=True)
    price               = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    order_created       = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering =['order_created']
