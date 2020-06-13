from django.db import models
from django.urls import reverse
from datetime import date

# Validators!!

def photo_path(instance, filename):
    return "student/" + str(instance.id) + "/photo/" + filename


class Field(models.Model):
    field_name = models.CharField(max_length=50, unique=True, verbose_name="Field name")
    field_short = models.CharField(max_length=5, unique=True, verbose_name="Field short name")

    class Meta:
        ordering = ["field_name"]

    def __str__(self):
        return self.field_short


class Address(models.Model):
    city_name = models.CharField(max_length=100, verbose_name="City")
    city_psc = models.IntegerField(verbose_name="City psc")

    class Meta:
        ordering = ["city_name", "city_psc"]

    def __str__(self):
        return f"{self.city_name} {self.city_psc}"


class Subject(models.Model):
    subject_name = models.CharField(max_length=50, verbose_name="Subject name", unique=True)
    subject_short = models.CharField(max_length=3, verbose_name="Subject short name", unique=True)

    class Meta:
        ordering = ["subject_name"]

    def __str__(self):
        return self.subject_short


class Teacher(models.Model):
    teacher_short = models.CharField(max_length=5, verbose_name="Teacher abbrev", unique=True)
    teacher_name = models.CharField(max_length=30, verbose_name="Teacher name")
    teacher_surname = models.CharField(max_length=50, verbose_name="Teacher surname")
    teacher_pid = models.CharField(max_length=11, verbose_name="Teacher pid (rodne cislo)", unique=True,
                                   help_text="Format - XXXXXX/XXXX")
    # teacher_subjects = models.ManyToManyField(Subject, help_text="Select teacher's subjects")

    class Meta:
        ordering = ["teacher_short"]

    def __str__(self):
        return f"{self.teacher_name} {self.teacher_surname} ({self.teacher_short})"


class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        ordering = ["teacher"]

    def __str__(self):
        return f"{self.subject} - {self.teacher}"


class Class(models.Model):
    class_name = models.CharField(max_length=50, verbose_name="Class name")
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, help_text="Select class subjects")

    class Meta:
        ordering = ["field", "class_name"]

    def __str__(self):
        return self.class_name


class Student(models.Model):
    student_pid = models.CharField(max_length=11, verbose_name="Student PID (rodne cislo)")
    student_name = models.CharField(max_length=30, verbose_name="Student name")
    student_surname = models.CharField(max_length=50, verbose_name="Student surname")
    student_city = models.ForeignKey(Address, on_delete=models.CASCADE)
    student_street = models.CharField(max_length=50, verbose_name="Street")
    student_house_number = models.IntegerField(verbose_name="House number")
    student_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    student_photo = models.ImageField(upload_to=photo_path, blank=True, null=True, verbose_name="Student photo")

    class Meta:
        ordering = ["student_surname", "student_name"]

    def __str__(self):
        return f"{self.student_name} {self.student_surname}, {self.student_class}"

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])


class Mark(models.Model):
    # Vybrat jestli Teacher a Subject zvlášť / ne - teď obojí napůl
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    # teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    teacher = models.ForeignKey(TeacherSubject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="title", max_length=50)
    MARK_CHOICES = (
        (1.0, "1.0"),
        (1.5, "1.5"),
        (2.0, "2.0"),
        (2.5, "2.5"),
        (3.0, "3.0"),
        (3.5, "3.5"),
        (4.0, "4.0"),
        (4.5, "4.5"),
        (5.0, "5.0"),
    )
    mark = models.DecimalField(verbose_name="Mark", max_digits=2, decimal_places=1, choices=MARK_CHOICES,
                               help_text="Select mark")

    MARK_WEIGHTS = (
        (10, "10%"),
        (20, "20%"),
        (30, "30%"),
        (40, "40%"),
        (50, "50%"),
        (60, "60%"),
        (70, "70%"),
        (80, "80%"),
        (90, "90%"),
        (100, "100%")
    )
    # decimal field - nejde
    # mark_weight = models.FloatField(verbose_name="Mark weight", choices=MARK_WEIGHTS, help_text="Select mark weight")
    mark_weight = models.IntegerField(verbose_name="Mark weight", choices=MARK_WEIGHTS, help_text="Select mark weight")
    date = models.DateField(verbose_name="Date", help_text="YYYY-MM-DD", default=date.today)
    comment = models.TextField(verbose_name="Comment", max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["-date", "student"]

    def __str__(self):
        return f"Student: {self.student}; {self.subject}, Teacher: {self.teacher}, Title: {self.title}, Mark: {self.mark}, Mark weight: {self.mark_weight}"
