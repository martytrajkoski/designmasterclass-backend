from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=200, null=True)
    lastName = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    dateCreated = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        template = '{0.firstName} | {0.lastName} | {0.username}'
        return template.format(self)
    # def __str__(self):
    #     return self.firstName, self.lastName, self.username

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

class Purchase(models.Model):
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    datePurchase = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        template = '{0.course} | {0.customer}'
        return template.format(self)
    
class TutorialPhotoshop(models.Model):
    name = models.CharField(max_length=500, null=True)
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    content5 = models.TextField(blank=True)
    image1 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image2 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image3 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image4 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image5 = models.ImageField(upload_to='./static/tutorial', blank=True)

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
    image1 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image2 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image3 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image4 = models.ImageField(upload_to='./static/tutorial', blank=True)
    image5 = models.ImageField(upload_to='./static/tutorial', blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
