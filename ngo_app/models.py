from django.db import models

class Volunteer(models.Model):
    vname = models.CharField(max_length=100)
    vphno = models.CharField(max_length=15)
    vemail = models.EmailField(max_length=100)
    vaddress = models.CharField(max_length=200)

    def __str__(self):
        return self.vname
class Contact(models.Model):
    cname =models.CharField(max_length=100)
    cemail=models.EmailField(max_length=100)
    csubject=models.CharField(max_length=150)
    cmessage =models.CharField(max_length=200)

    def __str__(self):
        return self.cname
    
class Donation(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)
    payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ₹{self.amount}"