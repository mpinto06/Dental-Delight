from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddAppointmentForm
from .models import Appointment
from django.contrib import messages

@login_required
def appointments_list(request):
    appointments = Appointment.objects.filter(created_by=request.user)
    return render(request, "appointments/appointments_list.html", {"appointments": appointments})

@login_required
def appointments_details(request, pk):
    appointment = get_object_or_404(request.user.appo, pk=pk)

    return render(request, "appointments/appointments_details.html", {"appointment": appointment})


@login_required
def appointments_add(request, fk):
    context = {"title": "Schedule Appointment"}
    if request.method == "POST":
        form = AddAppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.created_by = request.user
            appointment.patient_id = fk
            appointment.save()

            return redirect("appointments:list")
        else:
            context["form"] = form
            return render(request, "appointments/appointments_form.html", context)

    else:
        form = AddAppointmentForm()
        context["form"] = form
        return render(request, "appointments/appointments_form.html", context)

@login_required
def appointments_edit(request, pk):
    context = {"title": "Change Appointment"}
    appointment = get_object_or_404(request.user.appointments, pk=pk)
    if request.method == "POST":
        form = AddAppointmentForm(request.POST, instance=appointment)

        if form.is_valid():
            form.save()

            messages.success(request, 'The Appointment was changed successfully')
            
            return redirect("appointments:list")
        else:
            context["form"] = form
            return render(request, "appointments/appointments_form.html", context)

    else:
        form = AddAppointmentForm(instance=appointment)
        context["form"] = form
        return render(request, "appointments/appointments_form.html", context)

@login_required
def appointments_delete(request, pk):
    appointment = get_object_or_404(request.user.appointments, pk=pk)
    if request.method == "POST":
        appointment.delete()

        messages.success(request, 'The Appointment was removed succesfully! ')
        return redirect("appointments:list")

    else:
        return render(request, "appointments/appointments_delete.html", {"appointment": appointment})

    
