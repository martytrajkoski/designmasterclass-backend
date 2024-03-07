from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Insert email")
        if not password:
            raise ValueError('A password is required.')
        email = self.normalize_email(email)
        user =  self.model(email=email)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password):
        if not email:
            raise ValueError('An email is required.')
        if not password:
            raise ValueError('A password is required.')
        user = self.create_user(email, password)
        user.is_superuser = True
        user.save()
        return user

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
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        template = '{0.firstName} | {0.lastName} | {0.username}'
        return template.format(self)
    
    def has_module_perms(self, add_label):
        return True
    
    def has_perm(self, perm, obj=None):
        return True
    
class Quiz(models.Model):
    CATEGORY = (
        ('Photoshop', 'Photoshop'),
        ('Illustrator', 'Illustrator')
    )
    name = models.CharField(max_length=200, null=True)
    artist = models.CharField(max_length=50, null=True)
    length = models.DurationField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    url = models.URLField(max_length=200, null=True)
    thumbnail = models.ImageField(upload_to='./static/quiz', null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)

    @property
    def link(self):
        return f"/{self.url_slug}/"

class Course(models.Model):
    CATEGORY = (
        ('Photoshop', 'Photoshop'),
        ('Illustrator', 'Illustrator')
    )
    name = models.CharField(max_length=200, null=True)
    artist = models.CharField(max_length=50, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    # description = models.CharField(max_length=500, null=True)
    length = models.DurationField(null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    url = models.URLField(max_length=200, null=True)
    thumbnail = models.ImageField(upload_to='./static/course', null=True)

    def __str__(self):
        template = '{0.name} | {0.category}'
        return template.format(self)
    
    @property
    def link(self):
        return f"/{self.url_slug}/"
    
class CustomUserQuizzes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class CustomUserCourses(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

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
