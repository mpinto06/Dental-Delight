from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddDentistForm
from .models import Dentist
from django.contrib import messages

@login_required
def dentists_list(request):
    dentists = Dentist.objects.filter(created_by=request.user)
    return render(request, "dentists/dentists_list.html", {"dentists": dentists})

@login_required
def dentists_details(request, pk):
    dentist = get_object_or_404(request.user.dentists, pk=pk)

    return render(request, "dentists/dentists_details.html", {"dentist": dentist})


@login_required
def dentist_add(request):
    context = {"title": "Create New Dentist"}
    if request.method == "POST":
        form = AddDentistForm(request.POST)

        if form.is_valid():
            dentist = form.save(commit=False)
            dentist.created_by = request.user
            dentist.save()

            return redirect("dentists:list")
        else:
            context["form"] = form
            return render(request, "dentists/dentists_form.html", context)

    else:
        form = AddDentistForm()
        context["form"] = form
        return render(request, "dentists/dentists_form.html", context)

@login_required
def dentists_edit(request, pk):
    context = {"title": "Edit Dentist"}
    dentist = get_object_or_404(request.user.dentists, pk=pk)
    if request.method == "POST":
        form = AddDentistForm(request.POST, request.FILES, instance=dentist)

        if form.is_valid():
            dentist.save()

            messages.success(request, 'The Dentist was edited successfully')
            
            return redirect("dentists:list")
        else:
            context["form"] = form
            return render(request, "dentists/dentists_form.html", context)

    else:
        form = AddDentistForm(instance=dentist)
        context["form"] = form
        return render(request, "dentists/dentists_form.html", context)

@login_required
def dentists_delete(request, pk):
    dentist = get_object_or_404(request.user.dentists, pk=pk)
    if request.method == "POST":
        dentist.delete()

        messages.success(request, 'The Dentist was deleted succesfully! ')
        return redirect("dentists:list")

    else:
        return render(request, "dentists/dentists_delete.html", {"dentist": dentist})

    
