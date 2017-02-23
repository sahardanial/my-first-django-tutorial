from django.db import models
from django.urls import reverse
from django.utils import timezone


class Phone(models.Model):
    name = models.CharField(max_length=200, help_text="enter phone name")
    description = models.TextField(max_length=1000, help_text="enter a brif description about phone")
    photo = models.ImageField(upload_to='product_photo', blank=True)
    price = models.PositiveIntegerField(null=True)
    costomoption = models.ForeignKey('CostomOption', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('phone-detail', args=[str(self.id)])

    def __str__(self):
        return self. name


class PhoneSold(models.Model):
    buyer = models.ForeignKey('auth.User')
    product = models.CharField(max_length=30, null=True)
    time_of_purchase = models.DateTimeField(default=timezone.now)
    phonenumber = models.PositiveIntegerField()
    email = models.EmailField(max_length=30, null=True, help_text="example@gmail.com")
    address = models.CharField(max_length=100, null=True)


class CostomOption(models.Model):
    modell = models.CharField(max_length=30)
    cpu = models.CharField(max_length=200, help_text="enter a cpu of phone")
    RAMmemory = models.IntegerField(help_text="enter a RAM memory in gig")
    internalmemory = models.IntegerField()
    qualitycamera = models.IntegerField()

    def get_absolute_url(self):
        return reverse('costomoption-detail', args=[str(self.id)])

    def __str__(self):
        return '%s , %s' % (self.modell, self.cpu)


class Repository(models.Model):
    phone = models.ForeignKey('Phone', on_delete=models.CASCADE, null=True)
    numbers = models.IntegerField(null=True, blank=True)

    PHONE_STATUS = (
        ('a', 'Available'),
        ('u', 'Unavailable'),
        ('o', 'Outdated'),
    )

    status = models.CharField(max_length=1, choices=PHONE_STATUS,
                              blank=True, default='a', help_text='PHONE availability')

    def name(self):
        return self.phone.name

    def costomoption(self):
        return self.phone.costomoption

    def get_pk(self):
        return self.phone.pk
