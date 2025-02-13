from django.db import models
from groups.base_model import BaseModel
from django.utils.text import slugify
from django.urls import reverse
from groups.models import Group


class Student(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]


    photo = models.ImageField(upload_to='students_images')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    grade = models.CharField(max_length=100)
    address = models.TextField()
    parent_name = models.CharField(max_length=100)
    parent_email = models.EmailField(unique=100)
    parent_phone = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.first_name, self.last_name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.first_name, self.last_name)
            slug = base_slug
            counter = 1
            while Student.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Student, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse(
            'students:detail',
            kwargs={
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day,
                'slug': self.slug
            })

