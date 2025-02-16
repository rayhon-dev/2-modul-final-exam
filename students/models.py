from django.db import models
from groups.base_model import BaseModel
from django.utils.text import slugify
from django.urls import reverse
from groups.models import Group
from subjects.models import Subject


class Student(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    GRADE_LEVEL = [
        ('grade_9', 'Grade 9'),
        ('grade_10', 'Grade 10'),
        ('grade_11', 'Grade 11'),

    ]


    photo = models.ImageField(upload_to='students_images')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    grade_level = models.CharField(max_length=100, choices=GRADE_LEVEL, default='grade_9')
    address = models.TextField()
    parent_name = models.CharField(max_length=100)
    parent_email = models.EmailField(unique=True)
    parent_phone = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    subjects = models.ManyToManyField(Subject, related_name='students')
    slug = models.SlugField(unique=True)
    relationship = models.CharField(max_length=100)
    enrollment_date = models.DateField()


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

    def get_update_url(self):
        return reverse('students:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('students:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"