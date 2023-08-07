from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import BlogPost,EmbassyBooking,AirlineTicketReservation,TravelTour
from .forms import BlogPostForm,EmbassyBookingForm,AirlineTicketReservationForm,TravelTourForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        

        new_user = User.objects.create_user(username=email, email=email, password=password)
        
        return redirect('login')
    return render(request, 'registration.html')


def landing(request):
    if request.user.is_authenticated:
        return render(request, 'landing.html')
    else:
        return redirect('login')

def about_us(request):
    return render(request, 'contact.html')

def contact_us(request):
    return render(request, 'contact.html')

def home(request):
    return render(request,'home.html')
def services(request):
    return render(request, 'services.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name ='post_detail.html'
    context_object_name = ['post']
    
class BlogPostCreateView(LoginRequiredMixin,CreateView):
    model = BlogPost
    template_name = 'post_create.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('post_list')
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def book_appointment(request):
    if request.method == 'POST':
        form = EmbassyBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EmbassyBookingForm()
    
    return render(request, 'book_appointment.html', {'form': form})

def reserve_ticket(request):
    if request.method == 'POST':
        form = AirlineTicketReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = AirlineTicketReservationForm()
    
    return render(request, 'reserve_ticket.html', {'form': form})

def create_tour(request):
    if request.method == 'POST':
        form = TravelTourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TravelTourForm()
    
    return render(request, 'create_tour.html', {'form': form})

def tour_list(request):
    tours = TravelTour.objects.all()
    return render(request, 'tour_list.html', {'tours': tours})

def profile_view(request):
    user = request.user
    
    email = user.email
    username = user.username
    
    return render(request,'profile.html', {'email': email,'username': username})

def reset_password(request):
    if request.method=='POST':
        new_password = request.POST.get('new_password')
        
        request.user.set_password(new_password)
        request.user.save()
        
        return redirect('profile')
    
    return render(request,'reset_password.html')