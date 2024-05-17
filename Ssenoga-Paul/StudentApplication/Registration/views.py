from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def student_registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        course = request.POST.get('course')
        entry_scheme = request.POST.get('entry_scheme')
        intake = request.POST.get('intake')
        sponsorship = request.POST.get('sponsorship')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        residence = request.POST.get('residence')

        student = Student(
            first_name=first_name,
            last_name=last_name,
            course=course,
            entry_scheme=entry_scheme,
            intake=intake,
            sponsorship=sponsorship,
            gender=gender,
            date_of_birth=date_of_birth,
            residence=residence
        )
        student.save()

        return HttpResponse('Form submitted successfully!')

    return render(request, 'ciu.html')