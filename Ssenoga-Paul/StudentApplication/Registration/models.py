from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    COURSE_CHOICES = (
        ('CHS', 'Certificate in Health Science'),
        ('CAT', 'Certificate in Applied Technology'),
        ('BIT', 'Bachelor of Information Technology'),
        ('BBT', 'Bachelors in Business Technology'),
        ('MPH', 'Master of Public Health'),
    )
    course = models.CharField(max_length=3, choices=COURSE_CHOICES)

    ENTRY_SCHEME_CHOICES = (
        ('A_LEVEL', 'A-Level certificate'),
        ('ADULT', 'Adult/Mature Learning'),
        ('CERTIFICATE', 'Certificate'),
        ('DIPLOMA', 'Diploma'),
        ('BACHELORS', 'Bachelors'),
    )
    entry_scheme = models.CharField(max_length=200, choices=ENTRY_SCHEME_CHOICES)

    INTAKE_CHOICES = (
        ('JAN', 'January Intake'),
        ('MAY', 'May Intake'),
        ('AUG', 'August Intake'),
    )
    intake = models.CharField(max_length=3, choices=INTAKE_CHOICES)

    SPONSORSHIP_CHOICES = (
        ('PRIVATE', 'Private'),
        ('GOVERNMENT', 'Government'),
        ('BURSARY', 'Bursary'),
    )
    sponsorship = models.CharField(max_length=10, choices=SPONSORSHIP_CHOICES)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

    date_of_birth = models.DateField()
    residence = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.course}"


