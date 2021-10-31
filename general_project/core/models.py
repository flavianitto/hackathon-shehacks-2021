from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid

class User(models.Model):

    """Model representing a user's info."""

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cpf_cnpj = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15) 
    address = models.CharField(max_length = 254)
    number = models.CharField(max_length = 10)
    address_complement = models.CharField(max_length=30) 
    neighborhood = models.CharField(max_length = 30)
    city = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Bank(models.Model):

    """Model representing a Bank."""

    bank_id = models.AutoField(primary_key=True)
    code = models.IntegerField(max_length = 10)
    name = models.CharField(max_length=100)

USER_TYPE = (
        (0, "Receiver"),
        (1, "Donator")
    )

TRANSACTION_TYPE = (
        (0, "Money"),
        (1, "Food")
    )

class UserType(models.Model):

    """Model representing a user type."""

    user_type_id = models.AutoField(primary_key=True)
    user_type = models.IntegerField(choices=USER_TYPE, default=0)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, default=0)

class Partner(models.Model):

    """Model representing a parter's info."""

    partner_id = models.AutoField(primary_key=True)
    corporate_name = models.CharField(max_length=100)
    cpf_cnpj = models.CharField(max_length=20)
    cellphone = models.CharField(max_length=20)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15) 
    address = models.CharField(max_length = 254)
    number = models.CharField(max_length = 10)
    address_complement = models.CharField(max_length=30) 
    neighborhood = models.CharField(max_length = 30)
    city = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class UserInstance(models.Model):

    """Model representing a user instance's info."""

    record_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    user_type = models.ForeignKey(UserType, on_delete= models.CASCADE)
    account = models.ForeignKey(Bank, on_delete= models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)