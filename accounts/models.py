from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Insert email")
        email = self.normalize_email(email)
        user =  self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    firstName = models.CharField(max_length=255, null=True)
    lastName = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        template = '{0.firstName} | {0.lastName} | {0.username}'
        return template.format(self)
    
    def has_module_perms(self, add_label):
        return True
    
    def has_perm(self, perm, obj=None):
        return True

class Course(models.Model):
    CATEGORY = (
        ('Photoshop', 'Photoshop'),
        ('Illustrator', 'Illustrator')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=500, null=True)
    length = models.DurationField(null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    link = models.CharField(max_length=500, null=True)
    thumbnail = models.ImageField(upload_to='./static/course', null=True)

    def __str__(self):
        template = '{0.name} | {0.category}'
        return template.format(self)

# class Purchase(models.Model):
#     course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
#     customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
#     datePurchase = models.DateTimeField(auto_now_add=True, null=True)

#     def __str__(self):
#         template = '{0.course} | {0.customer}'
#         return template.format(self)
    
class TutorialPhotoshop(models.Model):
    name = models.CharField(max_length=500, null=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    content5 = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='./static/tutorial/', blank=True)
    image2 = models.ImageField(upload_to='./static/tutorial/', blank=True)
    image3 = models.ImageField(upload_to='./static/tutorial/', blank=True)
    image4 = models.ImageField(upload_to='./static/tutorial/', blank=True)
    image5 = models.ImageField(upload_to='./static/tutorial/', blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

class TutorialIllustrator(models.Model):
    name = models.CharField(max_length=500, null=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    content5 = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='./static/tutorialIllustrator/', blank=True)
    image2 = models.ImageField(upload_to='./static/tutorialIllustrator/', blank=True)
    image3 = models.ImageField(upload_to='./static/tutorialIllustrator/', blank=True)
    image4 = models.ImageField(upload_to='./static/tutorialIllustrator/', blank=True)
    image5 = models.ImageField(upload_to='./static/tutorialIllustrator/', blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
