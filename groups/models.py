from django.db import models
from groups.base_model import BaseModel
from django.utils.text import slugify
from teachers.models import Teacher
from subjects.models import Subject
from django.urls import reverse


class Group(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]


    name = models.CharField(max_length=100)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, related_name='group')
    academic_year = models.PositiveIntegerField()
    grade_level = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    max_students = models.PositiveIntegerField()
    desc = models.TextField()
    subjects = models.ManyToManyField(Subject, related_name='groups')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    slug = models.SlugField(unique=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Group.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Group, self).save(*args, **kwargs)


    def get_detail_url(self):
        return reverse(
            'groups:detail',
            kwargs={
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day,
                'slug': self.slug
            })
