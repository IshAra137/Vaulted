from django.db import models

# Create your models here.

#register form
class registertable(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Type=models.CharField(max_length=100)
    def __str__(self):
        return self.Name

#login form
class logintable(models.Model):
    Loginid = models.ForeignKey(registertable, on_delete=models.CASCADE, default=1)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Type = models.CharField(max_length=100)
    def __str__(self):
        return self.Name


# personal data
class personaltable(models.Model):
    Name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    address=models.CharField(max_length=500)
    Email = models.EmailField()
    number = models.IntegerField()
    Type = models.CharField(max_length=150)
    def __str__(self):
        return self.Name

# medical data
class medicaltable(models.Model):
    name = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_group = models.CharField(max_length=3)
    Gender = models.CharField(max_length=50)
    ill = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#academic data
class academictable(models.Model):
        Name = models.CharField(max_length=100)
        Hqul = models.CharField(max_length=100)
        Passout = models.IntegerField()
        Degree = models.CharField(max_length=100)
        Spec=models.CharField(max_length=500)
        inst = models.CharField(max_length=100)
        addt = models.CharField(max_length=500)
        Type = models.CharField(max_length=150)
        def __str__(self):
            return self.Name

#financial data
class financialtable(models.Model):
        Name = models.CharField(max_length=100)
        Bank_name= models.CharField(max_length=100)
        Account_number= models.IntegerField()
        Account_type = models.CharField(max_length=100)
        Investments=models.CharField(max_length=500)
        Assets = models.CharField(max_length=100)
        Credit_score = models.IntegerField()
        Type = models.CharField(max_length=150)
        def __str__(self):
            return self.Name

#docs data
class Document(models.Model):
    name = models.CharField(max_length=255)  # User's name
    tenth_certificate = models.FileField(upload_to='documents/tenth_certificates/')
    twelfth_certificate = models.FileField(upload_to='documents/twelfth_certificates/')
    degree_certificate = models.FileField(upload_to='documents/degree_certificates/')
    masters_certificate = models.FileField(upload_to='documents/masters_certificates/', blank=True, null=True)
    aadhar_card = models.FileField(upload_to='documents/aadhar_cards/')
    passport = models.FileField(upload_to='documents/passports/', blank=True, null=True)
    pan_card = models.FileField(upload_to='documents/pan_cards/', blank=True, null=True)

    def __str__(self):
        return self.name