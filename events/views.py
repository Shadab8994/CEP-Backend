from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Event, Registration, Feedback, UserProfile


# #  Role Helpers
# def is_admin(user):
#     return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'
def is_admin(user):

    # Django Superuser
    if user.is_superuser:
        return True

    # Custom Admin
    return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'

def is_student(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'student'


#  Home Page
@login_required
def event_list(request):

    query = request.GET.get('q')

    if query:
        events = Event.objects.filter(name__icontains=query)
    else:
        events = Event.objects.all()

    # Student Registration
    if request.method == "POST":

        if not is_student(request.user):
            return redirect('home')

        student_name = request.POST.get("student_name")
        event_id = request.POST.get("event_id")

        event = get_object_or_404(Event, id=event_id)

        Registration.objects.create(
            student_name=student_name,
            event=event
        )

        # return redirect('home')
        return redirect('/?registered=true')
    return render(request, 'events/index.html', {
        'events': events,
        'query': query,
        'is_admin': is_admin(request.user),
        'is_student': is_student(request.user),
    })


#  Registered Students (Admin Only)
@login_required
def registered_list(request):

    if not is_admin(request.user):
        return redirect('home')

    registrations = Registration.objects.all()

    return render(request, 'events/registered.html', {
        'registrations': registrations
    })


#  Feedback Page (Student Only)
@login_required
def feedback_view(request):

    if not is_student(request.user):
        return redirect('home')

    if request.method == 'POST':

        student_name = request.POST.get('student_name')
        message = request.POST.get('message')

        Feedback.objects.create(
            student_name=student_name,
            message=message
        )

        # return redirect('home')
        return redirect('/feedback/?feedback=success')

    return render(request, 'events/feedback.html')


#  Admin View Feedbacks
@login_required
def view_feedbacks(request):

    if not is_admin(request.user):
        return redirect('home')

    feedbacks = Feedback.objects.all()

    return render(request, 'events/view_feedbacks.html', {
        'feedbacks': feedbacks
    })


#  Signup
def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        # Password Validation
        if password != confirm_password:
            return render(request, 'events/signup.html', {
                'error': 'Passwords do not match'
            })

        # Username Check
        if User.objects.filter(username=username).exists():
            return render(request, 'events/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        UserProfile.objects.create(
            user=user,
            role=role
        )

        return redirect('login')

    return render(request, 'events/signup.html')


#  Login
def login_view(request):

    error = None

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')

        else:
            error = "Invalid username or password"

    return render(request, 'events/login.html', {
        'error': error
    })


#  Logout
def logout_view(request):

    logout(request)

    return redirect('login')

#  Add Event
@login_required
def add_event(request):

    if not is_admin(request.user):
        return redirect('home')

    if request.method == 'POST':

        name = request.POST.get('name')
        date = request.POST.get('date')
        location = request.POST.get('location')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Event.objects.create(
            name=name,
            date=date,
            location=location,
            description=description,
            status=status
        )

        return redirect('home')

    return render(request, 'events/add_event.html')


#  Edit Event
@login_required
def edit_event(request, event_id):

    if not is_admin(request.user):
        return redirect('home')

    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':

        event.name = request.POST.get('name')
        event.date = request.POST.get('date')
        event.location = request.POST.get('location')
        event.description = request.POST.get('description')
        event.status = request.POST.get('status')
        event.save()

        return redirect('home')

    return render(request, 'events/edit_event.html', {
        'event': event
    })


#  Delete Event
@login_required
def delete_event(request, event_id):

    if not is_admin(request.user):
        return redirect('home')

    event = get_object_or_404(Event, id=event_id)

    event.delete()

    return redirect('home')