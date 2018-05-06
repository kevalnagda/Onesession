from .forms import UserForm, ConForm, ChangeForm
from django.forms import ModelForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import FormDetails, UserDetails,  ChangeUserDetails

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password']
        user = UserDetails.objects.get(username=username)
        if user is not None:
            password2 = user.password
            if password1 == password2:
                if user.access:
                    return details(request)
                else:
                    return render(request, 'concession/index.html')
            else:
                return render(request, 'concession/login.html', {'error_message': 'Invalid login'})
    return render(request, 'concession/login.html')


def logout(request):
    return render(request, 'concession/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        if user is not None:
            return render(request, 'concession/login.html')
    context = {
        "form": form,
    }
    return render(request, 'concession/register.html', context)


def create_conform(request):
    form = ConForm(request.POST or None)
    if form.is_valid():
        conform = form.save(commit=False)
        conform.save()
        return render(request, 'concession/thanks.html')
    context = {"form": form}
    return render(request, 'concession/create_conform.html', context)


def index(request):
    return render(request, 'concession/index.html')


def info(request, form_id):
    form = FormDetails.objects.filter(sap=form_id)
    user = UserDetails.objects.get(sap=form_id)
    return render(request, 'concession/info.html', {'form': form, 'sap': form_id, 'user': user})


def Formstatus(request, form_id):
    f = FormDetails.objects.get(sap=form_id)
    f.status = True
    f.save()
    return details(request)


def editinfo(request, form_id):
    form = ChangeUserDetails.objects.filter(sap=form_id)
    return render(request, 'concession/editinfo.html', {'form': form, 'sap': form_id})


def userstatus(request, form_id):
    f = ChangeUserDetails.objects.get(sap=form_id)
    f.status = True
    f.save()
    return edit(request)


def edit(request):
    form_detail = ChangeUserDetails.objects.all()
    return render(request, 'concession/edit.html', {'form': form_detail})


def change(request):
    form = ChangeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        change_form = form.save(commit=False)
        change_form.save()
        change_form.address_proof = request.FILES['address_proof']
        file_type = change_form.address_proof.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'concession/change.html', context)
        change_form.save()
        return render(request, 'concession/thanks.html')
    context = {"form": form}
    return render(request, 'concession/change.html', context)


def details(request):
    form_detail = FormDetails.objects.all()
    return render(request, 'concession/detail.html', {'form': form_detail})
