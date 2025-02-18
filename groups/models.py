from django.db import models
from groups.base_model import BaseModel
from django.utils.text import slugify
from teachers.models import Teacher
from django.urls import reverse


class Group(BaseModel):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    GRADE_LEVEL = [
        ('grade_9', 'Grade 9'),
        ('grade_10', 'Grade 10'),
        ('grade_11', 'Grade 11'),

    ]

    SCHEDULE_CHOICES = [
        ('morning_session', 'Morning Session'),
        ('afternoon_session', 'Afternoon Session'),
        ('evening_session', 'Evening Session')
    ]


    name = models.CharField(max_length=100)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, related_name='group')
    academic_year = models.CharField(max_length=100)
    grade_level = models.CharField(max_length=100, choices=GRADE_LEVEL, default='grade_9')
    schedule = models.CharField(max_length=100, choices=SCHEDULE_CHOICES, default='morning_session')
    max_students = models.PositiveIntegerField()
    desc = models.TextField()
    subjects = models.ManyToManyField('subjects.Subject', related_name='groups')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    slug = models.SlugField(unique=100)

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

    def get_update_url(self):
        return reverse('groups:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('groups:delete', args=[self.pk])

    def __str__(self):
        return self.name