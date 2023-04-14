from django.urls import path

from . import views
from .views import show_books, student_borrowers, notifystaff, \
    notifydone, email_trigger, \
    staffborrowers, acceptstudentbook, acceptstaffbook, check_availability, student_borrower_info, finenacceptstaff, \
    finenacceptstudent, addbook, addstudentborrower, addstaffborrower, \
    staff_borrower_info, giveawaybookstudent, giveawaybookstaff, student_borrowed_books, \
    notifystudent, staff_borrowed_books, student_view_check_availability, endstudentmembership, endstaffmembership, \
    claimbook, displayclaimedbooks, book_info, notifyadmin

app_name = 'BooksnBorrowers'

urlpatterns = [
    path('allbooks/', show_books, name='show books'),
    path('studentborrowedbooks/', student_borrowed_books, name='student borrowed books'),
    path('staffborrowedbooks/', staff_borrowed_books, name='staff borrowed books'),
    path('bookinfo/<int:id>', book_info, name='book info'),
    path('student_borrowers/', student_borrowers, name='student_borrowers'),
    path('staffborrowers/', staffborrowers, name='staffborrowers'),
    path('studentborrowerinfo/<int:id>', student_borrower_info, name='student borrower info'),
    path('staffborrowerinfo/<int:id>', staff_borrower_info, name='staff borrower info'),
    path('notifystudent/<str:name>', notifystudent, name='notifystudent'),
    path('notifystaff/<str:name>', notifystaff, name='notifystaff'),
    path('emailtrigger/<str:email>', email_trigger, name='email_trigger'),
    path('notifydone/', notifydone, name='notifydone'),
    path('acceptstudentbook/<str:issued_book>', acceptstudentbook, name='acceptstudentbook'),
    path('acceptstaffbook/<str:issued_book>', acceptstaffbook, name='acceptstaffbook'),
    path('admin_view_check_availability/<str:serial_num>', check_availability, name='availability'),
    path('student_view_check_availability/<str:serial_num>', student_view_check_availability,
         name='student_view_check_availability'),
    path('finenacceptstaff/<int:issued_book>', finenacceptstaff, name='finenacceptstaff'),
    path('finenacceptstudent/<int:issued_book>', finenacceptstudent, name='finenacceptstudent'),
    path('addbook/', addbook, name='addbook'),
    path('addstudentborrower/', addstudentborrower, name='addstudentborrower'),
    path('addstaffborrower/', addstaffborrower, name='addstaffborrower'),
    path('giveawaybookstudent/', giveawaybookstudent, name='giveawaybookstudent'),
    path('giveawaybookstaff/', giveawaybookstaff, name='giveawaybookstaff'),
    path('endstudentmembership/<str:student_id>', endstudentmembership, name='endstudentmembership'),
    path('endstaffmembership/<str:staff_id>', endstaffmembership, name='endstaffmembership'),
    path('claimbook/', claimbook, name='claimbook'),
    path('claimedbooks/', displayclaimedbooks, name='displayclaimedbooks'),
    path('notifyadmin/<str:name>/<str:edition>/<str:author>', notifyadmin, name='notifyadmin'),
    path('', views.index, name='index'),

]
