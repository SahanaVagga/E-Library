from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.template.loader import get_template

from E_Library.settings import LOGIN_URL
from .forms import AddBookForm, StaffBorrowerForm, StudentBorrowerForm, BooksTakenAwayStudentForm, \
    BooksTakenAwayStaffForm, ClaimBookForm
from .forms import UserRegisterForm
# Create your views here.
from .models import Book, StudentBorrower, StaffBorrower, BooksTakenAwaybyStudents, BooksTakenAwaybyStaff, BooksClaimed

ERROR_ADMIN_MSG = "Sorry, Only Librarian or Admin are permitted."
STUDENT_USERNAME_STARTS = 'm1815'
LIBRARAIAN_USRNAME_STARTS = 'libraria'


def home(request):
    return render(request, 'firstfile.html')


@login_required(login_url=LOGIN_URL)
def welcome(request):
    username = str(request.user).lower()
    if username.startswith(STUDENT_USERNAME_STARTS): # re-direct to student view
        return render(request, "index.html", {'books': Book.objects.all()})
    elif username.startswith(LIBRARAIAN_USRNAME_STARTS): # re-direct to librarian view
        return render(request, 'books.html', {'books': Book.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def show_books(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        return render(request, 'books.html', {'books': Book.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def book_info(request, id):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        book = get_object_or_404(Book, pk=id)
        return render(request, 'book.html', {'book': book})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def student_borrowed_books(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        return render(request, 'student_borrowed_books.html', {'books': BooksTakenAwaybyStudents.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')

@login_required(login_url=LOGIN_URL)
def staff_borrowed_books(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        return render(request, 'staff_borrowed_books.html', {'books': BooksTakenAwaybyStaff.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')

@login_required(login_url=LOGIN_URL)
def student_borrowers(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        return render(request, 'studentborrowers.html', {'books': StudentBorrower.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def student_borrower_info(request, id):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        borrower = get_object_or_404(StudentBorrower, pk=id)
        print("The value of Books is", borrower)
        return render(request, 'student_borrower_info.html', {'borrower': borrower})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def staff_borrower_info(request, id):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        borrower = get_object_or_404(StaffBorrower, pk=id)
        print("The value of Books is", borrower)
        return render(request, 'staff_borrower_info.html', {'borrower': borrower})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def staffborrowers(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        return render(request, 'staffborrowers.html', {'books': StaffBorrower.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def staff_borrower_info(request, id):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        borrower = get_object_or_404(StaffBorrower, pk=id)
        print("The value of Books is", borrower)
        return render(request, 'staff_borrower_info.html', {'borrower': borrower})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def notifystudent(request, name):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        name = name.split()
        print(name)
        borrower_details = StudentBorrower.objects.filter(Firstname=name[0]).filter(Lastname=name[1])
        return render(request, 'notifystudent.html', {'borrower_details': borrower_details[0]})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def notifystaff(request, name):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        name = name.split()
        print(name)
        borrower_details = StaffBorrower.objects.filter(Firstname=name[0]).filter(Lastname=name[1])
        print(borrower_details)
        return render(request, 'notifystaff.html', {'borrower_details': borrower_details[0]})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def notifydone(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        return render(request, 'notifydone.html')
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def email_trigger(request, email):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        try:
            status = send_mail('E-Library Warning on Delay in Returning Book',
                               'One or more books are attracting fines for late renewal or return. Please contact Librarian to '
                               'avoid further fines and cancellation of membership at worst case. Thanks!!',
                               'mylibrary1095@gmail.com', [email])
            return render(request, 'notifydone.html')
        except Exception as e:
            return HttpResponse(f"Mail sending has failed!!. {e}")
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def acceptstudentbook(request, issued_book):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        BooksTakenAwaybyStudents.objects.filter(id=issued_book).delete()
        return render(request, 'student_borrowed_books.html', {'books': BooksTakenAwaybyStudents.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def acceptstaffbook(request, issued_book):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        BooksTakenAwaybyStaff.objects.filter(id=issued_book).delete()
        return render(request, 'student_borrowed_books.html', {'books': BooksTakenAwaybyStaff.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def finenacceptstudent(request, issued_book):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        book = BooksTakenAwaybyStudents.objects.get(id=issued_book)
        book = book.Borrower_issued_book
        book.book_total_fine_collected += 50
        book.book_late_renewal_count += 1
        book.save()
        BooksTakenAwaybyStudents.objects.filter(id=issued_book).delete()
        return render(request, 'student_borrowed_books.html', {'books': BooksTakenAwaybyStudents.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def finenacceptstaff(request, issued_book):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        book = BooksTakenAwaybyStaff.objects.get(id=issued_book)
        book = book.Borrower_issued_book
        book.book_total_fine_collected += 50
        book.book_late_renewal_count += 1
        book.save()
        BooksTakenAwaybyStaff.objects.filter(id=issued_book).delete()
        return render(request, 'student_borrowed_books.html', {'books': BooksTakenAwaybyStaff.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def check_availability(request, serial_num):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        student_borrowed_books = BooksTakenAwaybyStudents.objects.all()
        staff_borrowed_books = BooksTakenAwaybyStaff.objects.all()
        all_borrowed_books = list(student_borrowed_books) + list(staff_borrowed_books)
        print(all_borrowed_books)
        print("Got is ", serial_num)
        if len(all_borrowed_books) == 0:
            mybook = Book.objects.get(book_serial_number=serial_num)
            mybook.book_availability = 'Yes'
            mybook.save()
            return render(request, 'books.html', {'books': Book.objects.all()})

        for book in all_borrowed_books:
            print("book now is: ", book)
            print("book type now is: ", type(book))
            book = book.Borrower_issued_book
            mybook = Book.objects.get(book_serial_number=serial_num)
            if int(book.book_serial_number) == int(serial_num):
                mybook.book_availability = 'No'
                mybook.save()
        return render(request, 'books.html', {'books': Book.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def student_view_check_availability(request, serial_num):
    if str(request.user).lower().startswith(STUDENT_USERNAME_STARTS):
        student_borrowed_books = BooksTakenAwaybyStudents.objects.all()
        staff_borrowed_books = BooksTakenAwaybyStaff.objects.all()
        all_borrowed_books = list(student_borrowed_books) + list(staff_borrowed_books)
        print(all_borrowed_books)
        print("Got is ", serial_num)
        if len(all_borrowed_books) == 0:
            print('in 0')
            mybook = Book.objects.get(book_serial_number=serial_num)
            mybook.book_availability = 'Yes'
            mybook.save()
            return render(request, 'index.html', {'books': Book.objects.all()})

        for book in all_borrowed_books:
            print("book now is: ", book)
            print("book type now is: ", type(book))
            book = book.Borrower_issued_book
            mybook = Book.objects.get(book_serial_number=serial_num)
            print(int(book.book_serial_number))
            print(int(serial_num))
            if int(book.book_serial_number) == int(serial_num):
                mybook.book_availability = 'No'
                mybook.save()
        return render(request, 'index.html', {'books': Book.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def addbook(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        form = AddBookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request, "addbook.html", {'form': form})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def addstudentborrower(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        form = StudentBorrowerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request, "addstudent.html", {'form': form})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def addstaffborrower(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        form = StaffBorrowerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request, "addstaff.html", {'form': form})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def giveawaybookstudent(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        form = BooksTakenAwayStudentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request, "giveaway.html", {'form': form})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def giveawaybookstaff(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        form = BooksTakenAwayStaffForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request, "giveaway.html", {'form': form})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


def endstudentmembership(request, student_id):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        StudentBorrower.objects.get(Student_id=student_id).delete()
        return render(request, "studentborrowers.html", {'books': StudentBorrower.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def endstaffmembership(request, staff_id):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        StaffBorrower.objects.get(Staff_id=staff_id).delete()
        return render(request, "staffborrowers.html", {'books': StaffBorrower.objects.all()})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def claimbook(request):
    if str(request.user).lower().startswith(STUDENT_USERNAME_STARTS):
        form = ClaimBookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
        return render(request, "claimbook.html", {'form': form})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def displayclaimedbooks(request):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        books = BooksClaimed.objects.all()
        return render(request, 'displayclaimedbooks.html', {'books': books})
    else:
        messages.info(request, f'{ERROR_ADMIN_MSG}')
        return redirect('logout')


@login_required(login_url=LOGIN_URL)
def notifyadmin(request, name, edition, author):
    if str(request.user).lower().startswith(LIBRARAIAN_USRNAME_STARTS):
        Subject = 'Requesting Book to be added to Library Inventory based on Students Request.'
        Message = f'Hello Admin\n I, the Librarain has noticed a request for a book named {name} with edition {edition} by author {author}. Please take care to add it as soon as possible. \n \n Thanks\nLibrarian'
        try:
            status = send_mail(Subject,
                               Message,
                               'bcaelibrary@gmail.com', ['bcaelibrary@gmail.com'])
            return render(request, 'notifydone.html')
        except Exception as e:
            return HttpResponse(f"Mail sending has failed!!. {e}")
    else:
        messages.info(request,  f'{ERROR_ADMIN_MSG}')
        return redirect('logout')

#################### index#######################################
def index(request):
    return render(request, 'homepage.html', {'title': 'index'})


########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            email = form.cleaned_data.get('email')
            firstname = form.cleaned_data.get('first_name')
            ######################### mail system ####################################
            htmly = get_template('email.html')
            d = {'username': username, 'password': password, 'firstname': firstname}
            subject, from_email, to = 'welcome', 'bcaelibrary@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'Account Created. Check your Inbox!!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form, 'title': 'reqister here'})


################ login forms###################################################
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            # messages.success(request, f' welcomeeeee {username} !!')
            return redirect('welcome')
        else:
            messages.info(request, f'account does not exist')
            return redirect('login')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})
