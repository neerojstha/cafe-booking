from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Post, Menu
from .forms import BookingForm
from .models import Booking
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
            },
        )

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

@login_required
def booking_list(request):
    if request.user.is_staff:
        # If the user is a superuser, display all bookings
        bookings = Booking.objects.filter(canceled=False)
    else:
        # For regular users, display their own bookings
        bookings = Booking.objects.filter(email=request.user.email, canceled=False)

    return render(request, 'booking_list.html', {'bookings': bookings})

# The view for superusers to see all bookings
@staff_member_required
def superuser_booking_list(request):
    bookings = Booking.objects.filter(canceled=False)
    return render(request, 'superuser_booking_list.html', {'bookings': bookings})

@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_edit.html', {'form': form, 'booking': booking})

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    if request.method == 'POST':
        booking.cancel_booking()
        return redirect('booking_list')
    return render(request, 'booking_confirm_delete.html', {'booking': booking})

def menu(request):
    items = Menu.objects.all()
    return render(request, 'menu.html', {'items': items})

def contact(request):
    return render(request, 'contact.html') 