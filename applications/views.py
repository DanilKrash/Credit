from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from applications.forms import CreditForm

from applications.models import Credit


@login_required(login_url='auth:sign-in')
def send_applic(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('applic:send_applic')
    form = CreditForm()
    return render(request, 'applications/send_applic.html', {'form': form})


@login_required(login_url='auth:sign-in')
def whating_applic(request):
    applic = Credit.objects.filter(user=request.user)
    return render(request, 'applications/whating_applic.html', {'applic': applic})


@staff_member_required()
def all_applic(request):
    applic = Credit.objects.all
    return render(request, 'applications/all_applic.html', {'applic': applic})


@staff_member_required()
def change_status(request, applic_id):
    applic = get_object_or_404(Credit, id=applic_id)

    if request.method == 'POST':

        new_status = request.POST.get('status')
        applic.status = new_status
        applic.save()

    return render(request, 'applications/change_status.html', {'applic': applic})


