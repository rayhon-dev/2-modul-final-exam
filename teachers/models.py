from django.db import models
from groups.base_model import BaseModel
from django.utils.text import slugify
from subjects.models import Subject
from django.urls import reverse



class Teacher(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('on_leave', 'On Leave'),
    ]

    EMPLOYMENT_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time '),
        ('contract', 'Contract')
    ]

    photo = models.ImageField(upload_to='teachers_photos/')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    department = models.ForeignKey('departments.Department', on_delete=models.SET_NULL, null=True, related_name='teachers')
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    qualification = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=100, choices=EMPLOYMENT_TYPES, default='full_time')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    slug = models.SlugField(unique=True)
    joined_date = models.DateField()
    position = models.CharField(max_length=100)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # @property
    # def group_count(self):
    #     return self.groups.count()

    # @property
    # def student_count(self):
    #     return self.students.count()

    @property
    def subject_names(self):
        return ', '.join([subject.name for subject in self.subjects.all()])

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name}-{self.last_name}")
            slug = base_slug
            counter = 1
            while Teacher.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Teacher, self).save(*args, **kwargs)


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
        return reverse('teachers:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('teachers:delete', args=[self.pk])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
