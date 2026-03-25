from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Listing


def home(request):
    return render(request, '../templates/home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        role = request.POST.get('role', 'customer')

        if password != password_confirm:
            error_message = "Passwords do not match."
            return render(request, '../templates/register.html', {'error_message': error_message})

        user = User.objects.create_user(
            username=first_name + " " + last_name,
            email=email,
            password=password,
        )
        # Update the auto-created profile with the selected role
        user.profile.role = role
        user.profile.save()

        auth_login(request, user)

        if role == 'seller':
            return redirect('seller_dashboard')
        return redirect('home')

    return render(request, '../templates/register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_login(request, user)
            if hasattr(user, 'profile') and user.profile.role == 'seller':
                return redirect('seller_dashboard')
            return redirect('home')
        else:
            error_message = "Invalid email or password."
            return render(request, '../templates/login.html', {'error_message': error_message})

    return render(request, '../templates/login.html')


def logout(request):
    auth_logout(request)
    return redirect('home')


# --- Seller decorator and views ---

def seller_required(view_func):
    """Decorator that checks user is a logged-in seller."""
    @login_required(login_url='login')
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, 'profile') or request.user.profile.role != 'seller':
            return redirect('home')
        return view_func(request, *args, **kwargs)
    wrapper.__name__ = view_func.__name__
    return wrapper


@seller_required
def seller_dashboard(request):
    listings = Listing.objects.filter(seller=request.user)
    total_impressions = listings.aggregate(total=models.Sum('impressions'))['total'] or 0
    active_count = listings.filter(is_active=True).count()
    context = {
        'listings': listings,
        'total_impressions': total_impressions,
        'active_count': active_count,
    }
    return render(request, '../templates/seller_dashboard.html', context)


@seller_required
def create_listing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')

        Listing.objects.create(
            seller=request.user,
            title=title,
            description=description,
            image=image,
            price=price if price else None,
        )
        return redirect('seller_dashboard')

    return render(request, '../templates/create_listing.html')


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id, is_active=True)
    # Increment impressions only for non-owner views
    if not request.user.is_authenticated or request.user != listing.seller:
        Listing.objects.filter(id=listing_id).update(impressions=models.F('impressions') + 1)
    return render(request, '../templates/listing_detail.html', {'listing': listing})
