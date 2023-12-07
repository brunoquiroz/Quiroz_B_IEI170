from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listar_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'listar_reservas.html', {'reservas': reservas})

def agregar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm()
    return render(request, 'agregar_reserva.html', {'form': form})

def modificar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('listar_reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'modificar_reserva.html', {'form': form, 'reserva': reserva})

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    reserva.delete()
    return redirect('listar_reservas')
