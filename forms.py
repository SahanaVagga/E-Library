from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Book, StaffBorrower, StudentBorrower, BooksTakenAwaybyStudents, \
    BooksTakenAwaybyStaff, BooksClaimed


# Create your forms here.
class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class StaffBorrowerForm(forms.ModelForm):
    class Meta:
        model = StaffBorrower
        fields = '__all__'


class StudentBorrowerForm(forms.ModelForm):
    class Meta:
        model = StudentBorrower
        fields = '__all__'


class BooksTakenAwayStudentForm(forms.ModelForm):
    class Meta:
        model = BooksTakenAwaybyStudents
        fields = '__all__'


class BooksTakenAwayStaffForm(forms.ModelForm):
    class Meta:
        model = BooksTakenAwaybyStaff
        fields = '__all__'


class ClaimBookForm(forms.ModelForm):
    class Meta:
        model = BooksClaimed
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'password1', 'password2']
