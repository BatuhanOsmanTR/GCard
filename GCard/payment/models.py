from django.db import models
from django.conf import settings
import uuid

def card_digit_gen ():
    return uuid.uuid4().hex[:8]

class Card(models.Model):
     digits = models.CharField(max_length=8, default=card_digit_gen, unique=True)
     balance = models.PositiveSmallIntegerField()


class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField()
    image = models.URLField()

def paymentcard_digit_gen():
    return uuid.uuid4().hex[:10]

class PaymentCard(models.Model):
    digits = models.CharField(max_length=10, default=paymentcard_digit_gen, unique=True)
    balance = models.PositiveSmallIntegerField()
    used = models.BooleanField(default=False)
        def __str__(self):
        return "Card No: {dig} \n Card Balance: {bal} \n Is Card Used: {used} ".format(dig=self.digits, bal=self.balance, used=self.used)
