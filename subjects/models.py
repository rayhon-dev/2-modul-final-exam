from django.db import models
from groups.base_model import BaseModel
from django.utils.text import slugify
from departments.models import Department
from  django.urls import reverse


class Subject(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    GRADE_LEVEL = [
        ('grade_9', 'Grade 9'),
        ('grade_10', 'Grade 10'),
        ('grade_11', 'Grade 11'),

    ]

    PREREQUISITES_CHOICES= [
        ('math', 'Basic Mathematics'),
        ('physics', 'Introduction to Physics'),
        ('chemistry', 'Basic Chemistry'),
        ('english', 'English Language')
    ]
    LEVELS_CHOICES = [
        ('advanced', 'Advanced Level'),
        ('intermediate', 'Intermediate Level'),
        ('beginner', 'Beginner Level'),
    ]

    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='subjects')
    desc = models.TextField()
    credit_hours = models.PositiveIntegerField()
    grade_level = models.CharField(max_length=100, choices=GRADE_LEVEL, default='grade_9')
    prerequisites = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    levels = models.CharField(max_length=100, choices=LEVELS_CHOICES, default='beginner')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    @property
    def teacher_count(self):
        return self.teachers.count()

    @property
    def student_count(self):
        return self.students.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Subject.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Subject, self).save(*args, **kwargs)


    def get_detail_url(self):
        return reverse(
            'subjects:detail',
            kwargs={
                'year': self.created_at.year,
                'month': self.created_at.month,
                'day': self.created_at.day,
                'slug': self.slug
            })
    def get_update_url(self):
        return reverse('departments:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('departments:delete', args=[self.pk])



