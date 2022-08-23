from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from main.models import Contact
from vehicle.models import Booking, Vehicles
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    mydata = Vehicles.objects.all()[:4]
    return render(request, "frontend/index.html", {'vehicles': mydata})

def vehicles(request):
    mydata = Vehicles.objects.all()
    return render(request, "frontend/car.html", {'vehicles': mydata})

def about(request):
    return render(request, "frontend/about.html")

def contact(request):
    return render(request, "frontend/contact.html")

def saveContact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']

        md = Contact(name=name, email=email, phone=phone, comment=comment)
        md.save()
    return redirect(contact)

def vehicleDetails(request,vehicleid):
    vehicle = Vehicles.objects.get(id=vehicleid)
    related = Vehicles.objects.all()[:3]
    return render(request, "frontend/car-single.html", {'vehicle': vehicle, 'related': related})

def bookNow(request, car_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pick_location = request.POST['pick_location']
            drop_location = request.POST['drop_location']
            pick_date = request.POST['pick_date']
            drop_date = request.POST['drop_date']
            pick_time = request.POST['pick_time']
            if len(pick_location) > 0 or len(drop_location) > 0 or len(pick_date) > 0 or len(drop_date) > 0 or (pick_time):
                car = Vehicles.objects.get(id=car_id)
                vehicle = car
                user = request.user
                book = Booking(vehicle=vehicle, user=user, pick_location=pick_location, drop_location=drop_location, pick_date=pick_date, drop_date=drop_date, pick_time=pick_time)
                book.save()
                messages.success(request, "Your booking is submited.")
                return redirect('/')
            else:
                messages.error(request, "FIll All the fields of form")
                return redirect(f'/book_now/{car_id}')

        else:
            messages.error(request, "Please Login First.")
    vehicle = Vehicles.objects.get(id=car_id)
    return render(request, "frontend/pricing.html", {'data': vehicle})

# def bookNow(request, car_id):
#     vehicle = Vehicles.objects.get(id=car_id)
#     return render(request, "frontend/pricing.html", {'data': vehicle})

def services(request):
    return render(request, "frontend/services.html")

def handleSignup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')

        if password != confirm_password:
            messages.error(request, "Confirm password do not match")
            return redirect('home')


        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, "Your AnyBlog Account has been created successfully.")
        return redirect('home')
    else:
        return HttpResponse("404 - The request page not found.!")

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Are logged in succesfully.")
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentials, please try again.")
            return redirect('home')

def handleLogout(request):
    if request.method == 'GET':
        logout(request)
        messages.success(request, "Logged out successfully.")
        return redirect('home')
