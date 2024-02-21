from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddPatientForm
from .models import Patient
from django.contrib import messages

@login_required
def patients_list(request):
    patients = Patient.objects.filter(created_by=request.user)
    return render(request, "patients/patients_list.html", {"patients": patients})

@login_required
def patients_details(request, pk):
    patient = get_object_or_404(request.user.patients, pk=pk)

    return render(request, "patients/patients_details.html", {"patient": patient})


@login_required
def patients_add(request):
    context = {"title": "Create New Patient"}
    if request.method == "POST":
        form = AddPatientForm(request.POST)

        if form.is_valid():
            patient = form.save(commit=False)
            patient.created_by = request.user
            patient.save()

            return redirect("patients:list")
        else:
            context["form"] = form
            return render(request, "patients/patients_form.html", context)

    else:
        form = AddPatientForm()
        context["form"] = form
        return render(request, "patients/patients_form.html", context)

@login_required
def patients_edit(request, pk):
    context = {"title": "Edit Patient"}
    patient = get_object_or_404(request.user.patients, pk=pk)
    if request.method == "POST":
        form = AddPatientForm(request.POST, instance=patient)

        if form.is_valid():
            patient.save()

            messages.success(request, 'The Patient was edited successfully')
            
            return redirect("patients:list")
        else:
            context["form"] = form
            return render(request, "patients/patients_form.html", context)

    else:
        form = AddPatientForm(instance=patient)
        context["form"] = form
        return render(request, "patients/patients_form.html", context)

@login_required
def patients_delete(request, pk):
    patient = get_object_or_404(request.user.patients, pk=pk)
    if request.method == "POST":
        patient.delete()

        messages.success(request, 'The Patient was deleted succesfully! ')
        return redirect("patients:list")

    else:
        return render(request, "patients/patients_delete.html", {"patient": patient})

    
