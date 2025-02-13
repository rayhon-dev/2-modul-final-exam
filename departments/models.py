from django.db import models
from groups.base_model import BaseModel
from django.utils.text import slugify
from django.urls import reverse



class Department(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey('teachers.Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='departments')
    desc = models.TextField()
    location = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    @property
    def teacher_count(self):
        return self.teachers.count()


    @property
    def subject_names(self):
        return ', '.join([subject.name for subject in self.subjects.all()])


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Department.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Department, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse(
            'teachers:detail',
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
