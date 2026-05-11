# from django.shortcuts import render
# from .models import Event

# def event_list(request):
#     events = Event.objects.all()
#     return render(request, 'events/index.html', {'events': events})

# from django.shortcuts import render, redirect
# from .models import Event, Registration

# def event_list(request):
#     if request.method == "POST":
#         name = request.POST.get("student_name")
#         event_id = request.POST.get("event_id")

#         event = Event.objects.get(id=event_id)

#         Registration.objects.create(
#             student_name=name,
#             event=event
#         )

#         return redirect('event_list')

#     events = Event.objects.all()
#     return render(request, 'events/index.html', {'events': events})

# def registered_list(request):
#     registrations = Registration.
#     return render(request, 'events/registered.html', {'registrations': registrations})
# from django.shortcuts import render
# from .models import Event

# def event_list(request):
#     query = request.GET.get('q')

#     if query:
#         events = Event.objects.filter(name__icontains=query)
#     else:
#         events = Event.objects.all()

#     return render(request, 'events/index.html', {
#         'events': events,
#         'query': query
#     })

# from django.shortcuts import render, redirect
# from .models import Feedback

# def feedback_view(request):
#     if request.method == 'POST':
#         student_name = request.POST.get('student_name')
#         message = request.POST.get('message')

#         Feedback.objects.create(
#             student_name=student_name,
#             message=message
#         )

#         return redirect('home')

#     return render(request, 'events/feedback.html')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration, Feedback


# 🔹 Home Page + Register + Search
def event_list(request):
    query = request.GET.get('q')

    # Search
    if query:
        events = Event.objects.filter(name__icontains=query)
    else:
        events = Event.objects.all()

    # Registration
    if request.method == "POST":
        name = request.POST.get("student_name")
        event_id = request.POST.get("event_id")

        event = get_object_or_404(Event, id=event_id)

        Registration.objects.create(
            student_name=name,
            event=event
        )

        return redirect('home')

    return render(request, 'events/index.html', {
        'events': events,
        'query': query
    })


# 🔹 Registered Events Page
def registered_list(request):
    registrations = Registration.objects.all()

    return render(request, 'events/registered.html', {
        'registrations': registrations
    })


# 🔹 Feedback Page
def feedback_view(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        message = request.POST.get('message')

        Feedback.objects.create(
            student_name=student_name,
            message=message
        )

        return redirect('home')

    return render(request, 'events/feedback.html')
