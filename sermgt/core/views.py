from django.shortcuts import render, redirect
from .models import Service, Appointement
from .forms import AddServiceForm, AppointementForm
# Create your views here.


def home(request):
    prods = Service.objects.all()
    return render(request, 'core/home.html', {'prods':prods})


def addservice(request):
    form = AddServiceForm(request.POST or None)
    if form.is_valid():
        abc = form.save(commit=False)
        abc.save()
        return redirect('home')
    else:
        form = AddServiceForm()
    return render(request, 'core/addservice.html', {'form':form})



def create_apt(request):
    service = request.POST.get("query")
    print(service)
    form = AppointementForm(request.POST or None, instance=service)
    if form.is_valid():
        service = form.save(commit=False)
        service.title = service
        service.save()
        return redirect('apts')
    form = AppointementForm()
    return render(request, 'core/create_apt.html', {'form':form})

def apts(request):
    qs = Appointement.objects.all()
    return render(request, 'core/appointements.html', {'qs':qs})
  