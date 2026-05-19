from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)

from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view

from rest_framework.response import Response

from .models import (
    Event,
    Registration,
    Feedback,
    UserProfile
)

from .serializers import EventSerializer
from django.contrib.auth import update_session_auth_hash



# 🔹 Role Helpers

def is_admin(user):

    if user.is_superuser:
        return True

    return (
        hasattr(user, 'userprofile')
        and user.userprofile.role == 'admin'
    )



def is_student(user):

    return (
        hasattr(user, 'userprofile')
        and user.userprofile.role == 'student'
    )



# 🔹 Home Page

@login_required
def event_list(request):

    query = request.GET.get('q')

    if query:

        events = Event.objects.filter(
            name__icontains=query
        )

    else:

        events = Event.objects.all()


    # 🔹 Student Registration

    if request.method == "POST":

        if not is_student(request.user):

            return redirect('home')


        student_name = request.POST.get(
            "student_name"
        ).strip().lower()


        event_id = request.POST.get(
            "event_id"
        )

        event = get_object_or_404(
            Event,
            id=event_id
        )


        # 🔹 Prevent Duplicate Registration

        already_registered = Registration.objects.filter(
            student_name=student_name,
            event=event
        ).exists()


        if already_registered:

            return redirect(
                '/?already_registered=true'
            )


        Registration.objects.create(
            student_name=student_name,
            event=event
        )

        return redirect(
            '/?registered=true'
        )


    return render(request, 'events/index.html', {

        'events': events,

        'query': query,

        'is_admin': is_admin(request.user),

        'is_student': is_student(request.user),

    })



# 🔹 Registered Students

@login_required
def registered_list(request):

    if not is_admin(request.user):

        return redirect('home')

    registrations = Registration.objects.all()

    return render(
        request,
        'events/registered.html',
        {
            'registrations': registrations
        }
    )



# 🔹 Feedback Page

@login_required
def feedback_view(request):

    if not is_student(request.user):

        return redirect('home')

    if request.method == 'POST':

        student_name = request.POST.get(
            'student_name'
        )

        message = request.POST.get(
            'message'
        )

        Feedback.objects.create(

            student_name=student_name,

            message=message

        )

        return redirect(
            '/feedback/?feedback=success'
        )

    return render(
        request,
        'events/feedback.html'
    )



# 🔹 View Feedbacks

@login_required
def view_feedbacks(request):

    if not is_admin(request.user):

        return redirect('home')

    feedbacks = Feedback.objects.all()

    return render(
        request,
        'events/view_feedbacks.html',
        {
            'feedbacks': feedbacks
        }
    )



# 🔹 Signup

def signup_view(request):

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        email = request.POST.get(
            'email'
        )

        password = request.POST.get(
            'password'
        )

        confirm_password = request.POST.get(
            'confirm_password'
        )

        role = request.POST.get(
            'role'
        )


        if password != confirm_password:

            return render(
                request,
                'events/signup.html',
                {
                    'error':
                    'Passwords do not match'
                }
            )


        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                'events/signup.html',
                {
                    'error':
                    'Username already exists'
                }
            )


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

    return render(
        request,
        'events/signup.html'
    )



# 🔹 Login

def login_view(request):

    error = None

    if request.method == 'POST':

        username = request.POST.get(
            'username'
        )

        password = request.POST.get(
            'password'
        )

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user:

            login(request, user)

            return redirect('home')

        else:

            error = (
                "Invalid username or password"
            )

    return render(
        request,
        'events/login.html',
        {
            'error': error
        }
    )



# 🔹 Logout

def logout_view(request):

    logout(request)

    return redirect('login')





# 🔹 Add Event

@login_required
def add_event(request):

    if not is_admin(request.user):

        return redirect('home')


    if request.method == 'POST':

        name = request.POST.get('name')

        date = request.POST.get('date')

        location = request.POST.get(
            'location'
        )

        description = request.POST.get(
            'description'
        )

        status = request.POST.get(
            'status'
        )


        Event.objects.create(

            name=name,

            date=date,

            location=location,

            description=description,

            status=status

        )

        return redirect('/?event_added=true')


    return render(
        request,
        'events/add_event.html'
    )



# 🔹 Edit Event

@login_required
def edit_event(request, event_id):

    if not is_admin(request.user):

        return redirect('home')


    event = get_object_or_404(
        Event,
        id=event_id
    )


    if request.method == 'POST':

        event.name = request.POST.get(
            'name'
        )

        event.date = request.POST.get(
            'date'
        )

        event.location = request.POST.get(
            'location'
        )

        event.description = request.POST.get(
            'description'
        )

        event.status = request.POST.get(
            'status'
        )

        event.save()

        return redirect('/?event_updated=true')


    return render(
        request,
        'events/edit_event.html',
        {
            'event': event
        }
    )



# 🔹 Delete Event

@login_required
def delete_event(request, event_id):

    if not is_admin(request.user):

        return redirect('home')


    event = get_object_or_404(
        Event,
        id=event_id
    )

    event.delete()

    return redirect('/?event_deleted=true')


# 🔹 Events API

@api_view(['GET'])
def event_api(request):

    events = Event.objects.all()

    serializer = EventSerializer(
        events,
        many=True
    )

    return Response(serializer.data)



# 🔹 Add Event API

@api_view(['POST'])
def add_event_api(request):

    serializer = EventSerializer(
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)



# 🔹 Update Event API

@api_view(['PUT'])
def update_event_api(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )

    serializer = EventSerializer(
        event,
        data=request.data
    )

    if serializer.is_valid():

        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors)

# 🔹 Event Detail Page

@login_required
def event_detail(request, event_id):

    event = get_object_or_404(
        Event,
        id=event_id
    )


    if request.method == "POST":


        # 🔹 Registration for Upcoming Events

        if event.status == "Upcoming":

            student_name = request.POST.get(
                "student_name"
            ).strip().lower()
            student_email = request.POST.get(
                "student_email"
            ).strip().lower()


            already_registered = Registration.objects.filter(
                student_email=student_email,
                event=event
            ).exists()

            if already_registered:

                return redirect(
                    f'/event/{event.id}/?already_registered=true'
                )


            Registration.objects.create(

                student_name=student_name,

                student_email=student_email,

                event=event

            )

            return redirect(
                f'/event/{event.id}/?registered=true'
            )



        # 🔹 Feedback for Ongoing / Completed Events

        else:

            student_name = request.POST.get(
                "student_name"
            )

            message = request.POST.get(
                "message"
            )


            Feedback.objects.create(

                student_name=student_name,

                event=event,

                message=message

            )

            return redirect(
                f'/event/{event.id}/?feedback=success'
            )


    return render(

        request,

        'events/event_detail.html',

        {

            'event': event,

            'is_student': is_student(request.user),

            'is_admin': is_admin(request.user),

        }
    )


    # 🔹 Registration

    if request.method == "POST":

        student_name = request.POST.get("student_name").strip().lower()
        already_registered = Registration.objects.filter(
            student_name=student_name,
            event=event
        ).exists()


        if already_registered:

            return redirect(
                f'/event/{event.id}/?already_registered=true'
            )


        Registration.objects.create(

            student_name=student_name,

            event=event

        )

        return redirect(
            f'/event/{event.id}/?registered=true'
        )


    return render(

        request,

        'events/event_detail.html',

        {

            'event': event,

            'is_student': is_student(request.user),

        }
    )

# 🔹 Change Username

@login_required
def change_username(request):

    if request.method == 'POST':

        new_username = request.POST.get(
            'username'
        )


        # Check Existing Username

        if User.objects.filter(
            username=new_username
        ).exists():

            return render(

                request,

                'events/change_username.html',

                {

                    'error':
                    'Username already exists'

                }
            )


        request.user.username = new_username

        request.user.save()

        return redirect('/')


    return render(
        request,
        'events/change_username.html'
    )
# 🔹 Change Password

@login_required
def change_password(request):

    if request.method == 'POST':

        old_password = request.POST.get(
            'old_password'
        )

        new_password1 = request.POST.get(
            'new_password1'
        )

        new_password2 = request.POST.get(
            'new_password2'
        )


        # 🔹 Wrong Old Password

        if not request.user.check_password(
            old_password
        ):

            return redirect(
                '/change-password/?password_error=true'
            )


        # 🔹 Password Mismatch

        if new_password1 != new_password2:

            return redirect(
                '/change-password/?password_mismatch=true'
            )


        # 🔹 Update Password

        request.user.set_password(
            new_password1
        )

        request.user.save()

        update_session_auth_hash(
            request,
            request.user
)


        return redirect(
            '/?password_changed=true'
        )


    return render(
        request,
        'events/change_password.html'
    )
