from datetime import timedelta

from django.db import models
from django.utils import timezone


# Create your models here.
class Book(models.Model):
    BOOK_HEALTH = (('Good', 'Good'), ('Average', 'Average'), ('Bad', 'Bad'))
    author_name = models.CharField(max_length=20, null=True)
    book_name = models.CharField(max_length=20, null=True)
    book_serial_number = models.CharField(unique=True, blank=False, max_length=6)
    book_price = models.IntegerField(default=300, null=True)
    published_year = models.IntegerField(default=2000, null=True)
    book_edition = models.DecimalField(max_digits=3, decimal_places=1, default=1.0, null=True)
    book_health = models.CharField(choices=BOOK_HEALTH, default='Good', max_length=20, null=True)
    book_availability = models.CharField(choices=(('Yes', 'Yes'), ('No', 'No')), default='Yes', max_length=3, null=True,
                                         editable=False)
    book_late_renewal_count = models.IntegerField(default=0, null=True, editable=False)
    book_total_fine_collected = models.IntegerField(default=0, null=True, editable=False)

    def __str__(self):
        return f"{self.book_name}-{self.book_edition} ({self.book_serial_number}) [Availabity = {self.book_availability}]"


class StudentBorrower(models.Model):
    Firstname = models.CharField(max_length=20, null=True)
    Lastname = models.CharField(max_length=20, null=True)
    Student_id = models.CharField(unique=True, blank=False, max_length=8)
    Email_id = models.EmailField(max_length=30, null=True, unique=True, )
    Student_address = models.CharField(max_length=50, null=True)
    Mobile = models.CharField(null=True, unique=True, max_length=10)
    Student_admitted_on = models.DateField(auto_now_add=True)
    Student_standard = models.CharField(max_length=20, choices=(
        ('1st Semester', '1st Semester'), ('2nd Semester', '2nd Semester'),
        ('3rd Semester', '3rd Semester'),
        ('4th Semester', '4th Semester'), ('5th Semester', '5th Semester'),
        ('6th Semester', '6th Semester')), default='1st Semester')

    def __str__(self):
        return f"{self.Firstname + ' ' + self.Lastname + ' ' + self.Student_id}"


class StaffBorrower(models.Model):
    Firstname = models.CharField(max_length=20, null=True)
    Lastname = models.CharField(max_length=20, null=True)
    Staff_id = models.CharField(unique=True, blank=False,
                                max_length=6)
    Staff_degree = models.CharField(choices=(('', ''), (
        'MCA', 'MCA'), ('B.Sc', 'B.Sc'), ('M.Sc', 'M.Sc'), ('B.E', 'B.E'), ('M.Tech', 'M.Tech')), default='MCA',
                                    null=True, max_length=6)
    Email_id = models.EmailField(max_length=30, null=True, unique=True)
    Staff_address = models.CharField(max_length=30, null=True)
    Mobile = models.CharField(null=True, unique=True, max_length=10)
    Staff_admitted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.Firstname + ' ' + self.Lastname + ' ' + self.Staff_id}"


class BooksTakenAwaybyStudents(models.Model):
    Borrower = models.ForeignKey(StudentBorrower, on_delete=models.CASCADE, null=True)
    Borrower_issued_book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    Borrower_book_issued_on = models.DateField(auto_now_add=True)
    Borrower_renewal_date = models.DateField(max_length=20,
                                             default=timezone.now().date() + timedelta(days=8))

    def __str__(self):
        return f"{self.Borrower_issued_book} - {self.Borrower}"


class BooksTakenAwaybyStaff(models.Model):
    Borrower = models.ForeignKey(StaffBorrower, on_delete=models.CASCADE, null=True)
    Borrower_issued_book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    Borrower_book_issued_on = models.DateField(auto_now_add=True)
    Borrower_renewal_date = models.DateField(max_length=20,
                                             default=timezone.now().date() + timedelta(days=7))

    def __str__(self):
        return f"{self.Borrower_issued_book} - {self.Borrower}"


class BooksClaimed(models.Model):
    Name = models.CharField(max_length=30, null=False, blank=False)
    Edition = models.DecimalField(max_digits=3, decimal_places=1, default=1.0, null=False, blank=False)
    Author = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f"{self.Name} +' '+'{self.Edition} +' ' +{self.Author}"
