from django.urls import path
from .views import BlogPostListView,create_tour,tour_list,register,book_appointment,reserve_ticket,BlogPostDetailView,BlogPostCreateView,login_view,landing,home,about_us,services,contact_us,profile_view,reset_password
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('login/',login_view,name='login'),
    path('register/',register,name='register'),
    path('home/',home,name='home'),
    path('about/',about_us,name='about'),
    path('services/',services,name='services'),
    path('contact_us/',contact_us, name='contact'),
    path('',landing,name='landing'),
    path('create-tour/', create_tour, name='create_tour'),
    path('tour-list/', tour_list, name='tour_list'),
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('', BlogPostListView.as_view(), name='post_list'),
    path('reserve-ticket/', reserve_ticket, name='reserve_ticket'),
    path('profile/',profile_view,name='profile'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('post/create/', BlogPostCreateView.as_view(), name='post_create'),
    path('reset_password',reset_password,name='reset_password'),
]
urlpatterns += staticfiles_urlpatterns()
