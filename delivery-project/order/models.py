from django.db import models

class BoyDetails(models.Model):
    boyname = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    boystatus = models.IntegerField()

    def __str__(self):
        return self.boyname


class Orders(models.Model):
    ordername = models.CharField(max_length=100)
    orderaddress = models.CharField(max_length = 300, default=None)
    deliveryboy = models.ForeignKey(BoyDetails, blank=True, null=True, on_delete = models.CASCADE)
    orderstatus = models.CharField(max_length=100)

    def __str__(self):
        return self.ordername


