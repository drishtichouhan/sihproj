from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator, int_list_validator
from django.conf import settings
import os.path


# Create your models here.

class User(AbstractBaseUser):
    USER_TYPE_CHOICES = (

        (1, 'complainant'),
        (2, 'volunteer'),
        (3, 'sho'),
        (4, 'witness'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=50, null=False, blank=False)
    father = models.CharField(max_length=50, null=True, blank=True)
    husband = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(blank=False)
    phone_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    aadhar_card = models.CharField(max_length=12, validators=[int_list_validator(sep=''), MinLengthValidator(12), ],
                                   default='1234567890')


class Complainant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class SHO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class FIR(models.Model):
    policeStation = models.CharField(max_length=50, null=False, blank=False)
    district = models.CharField(max_length=25, null=False, blank=False)
    STATE_TYPE_CHOICES = (('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'),
                          ('MH', 'Maharashtra'), ('UP', 'Uttar Pradesh'), ('GA', 'Goa'), ('GJ', 'Gujarat'),
                          ('RJ', 'Rajasthan'),
                          ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('TG', 'Telangana'),
                          ('AR', 'Arunachal Pradesh'),
                          ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chattisgarh'), ('HR', 'Haryana'),
                          ('JH', 'Jharkhand'),
                          ('MP', 'Madhya Pradesh'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'),
                          ('NL', 'Nagaland'),
                          ('OR', 'Orissa'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TR', 'Tripura'),
                          ('UA', 'Uttarakhand'), ('WB', 'West Bengal'),
                          ('AN', 'Andaman and Nicobar'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'),
                          ('DD', 'Daman and Diu'),
                          ('DL', 'Delhi'), ('LD', 'Lakshadweep'), ('PY', 'Pondicherry'))
    complainant_id = models.ForeignKey(Complainant, on_delete=models.CASCADE)
    place_of_occurence = models.TextField()
    time_of_occurence = models.DateField()
    time_when_registered = models.DateField()
    nature_of_offence = models.TextField()
    sections_under_crime_falls = models.TextField()
    description_of_accused = models.TextField()
    complaint = models.TextField()
    # audio_file = AudioField(upload_to='media/', blank=True, ext_whitelist=(".mp3", ".wav", ".ogg"))


class Witness(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    witness_for_fir = models.ForeignKey(FIR, on_delete=models.CASCADE)
    description = models.TextField(default="")
