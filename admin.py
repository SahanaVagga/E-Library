from django.contrib import admin

# Register your models here.
from .models import Book, StaffBorrower, StudentBorrower, BooksTakenAwaybyStudents, BooksTakenAwaybyStaff, BooksClaimed

admin.site.register([Book, StaffBorrower, StudentBorrower, BooksTakenAwaybyStudents, BooksTakenAwaybyStaff, BooksClaimed])
