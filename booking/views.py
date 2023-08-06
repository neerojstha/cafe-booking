from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Booking, Menu
from .forms import BookingForm

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "post_detail.html",
            {
                "post: post"
            },
        )

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  #
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def menu(request):
    items = Menu.objects.all()
    return render(request, 'menu.html', {'items': items})

def contact(request):
    return render(request, 'contact.html') 