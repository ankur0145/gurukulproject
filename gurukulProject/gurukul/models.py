from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from jsonfield import JSONField
class User(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=8,default=True)
    phone_no = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    meta = models.TextField(blank=True, null=True)
    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    

    
    def __str__(self):
        return self.email
   
class Course (models.Model):
    COURSE_CATEGORIES = [
        ('cat1', 'Category 1'),
        ('cat2', 'Category 2'),
        ('cat3', 'Category 3'),
        # Add more categories as needed
    ]

    category = models.CharField(max_length=10, choices=COURSE_CATEGORIES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=255)
    created_at = models.DateField()
    updated_at = models.DateField()
    
    meta = JSONField(null=True)
    
    # SEO field
    seo = JSONField()
    
    # Status field
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
        # Add more status options as needed
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.course_title

class Categories(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    description = models.CharField(max_length=255)
    seo = JSONField()
    meta = JSONField(null=True)

    def __str__(self):
        return self.title