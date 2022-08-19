from django.db import models

# Create your models here.

class Parcel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Courier_id = models.ForeignKey("Courier", on_delete=models.CASCADE, db_column="id3")
    Enroller_id = models.ForeignKey("Enroller", on_delete=models.CASCADE, db_column="id4")
    invoice_number = models.IntegerField()
    sender = models.CharField(max_length=10, blank=False, null=False)
    receiver = models.CharField(max_length=10, blank=False, null=False)
    product_name = models.CharField(max_length=30, blank=False, null=False)
    product_number = models.IntegerField()
    calculate = models.CharField(max_length=10, blank=False, null=False)
    fare = models.IntegerField()
    created = models.DateField(auto_now_add=True)


class Courier(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=40, blank=False, null=False)
    created = models.DateField(auto_now_add=True)


class Enroller(models.Model):
    id = models.BigAutoField(primary_key=True)
    Parcel_id = models.ForeignKey("Courier", on_delete=models.CASCADE, db_column="id2")
    user_id = models.CharField(max_length=20, blank=False, null=False)
    pwd = models.CharField(max_length=15, blank=False, null=False)
    name = models.CharField(max_length=10, blank=False, null=False)
    email = models.CharField(max_length=40, blank=False, null=False)
    phone_number = models.IntegerField()
    position = models.CharField(max_length=20, blank=False, null=False)
    created = models.DateField(auto_now_add=True)
