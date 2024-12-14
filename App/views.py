from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Tarea
from .forms import FormTarea
from django.utils import timezone


# Create your views here.

def Inicio(request):
    return render(request,'inicio.html')

def Registro(request):
    if request.method == 'GET':
        return render(request,'registro.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])  
                user.save()
                login(request, user)
                return redirect('tareas')
            except:
                return render(request,'registro.html',{
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        else:
            return render(request,'registro.html',{
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
        })
            
def Ingresar(request):
    if request.method == 'GET':
        return render(request,'ingresar.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request,username=request.POST['username'], password=request.POST['password'])  
        if user is None:
            return render(request,'ingresar.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('tareas')
        
def Salir(request):
    logout(request)
    return redirect('inicio')
    
def Tareas(request):
    tareas = Tarea.objects.filter(usuario=request.user, completado__isnull=True)
    return render(request, 'tareas.html',{
        'tareas': tareas
    })
        
def TareaCompleta(request):
    tareas = Tarea.objects.filter(usuario=request.user, completado__isnull=True).order_by
    ('-completado')
    return render(request, 'tareas.html',{
            'tareas': tareas
    })
    
def CrearTarea(request):
    if request.method == 'GET':
        return render(request, 'crear_tarea.html',{
            'form': FormTarea
        })
    else: 
        form = FormTarea(request.POST)
        tarea = form.save(commit=False)
        tarea.usuario = request.user
        tarea.save()
        return redirect('tareas')
    
def ActualizarTarea(request, tarea_id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk=tarea_id, usuario= request.user)
        form = FormTarea(instance=tarea)
        return render(request, 'actualizar.html', {
            'form': form,
            'tarea': tarea
        })
    else:
        tarea = get_object_or_404(Tarea, pk=tarea_id, usuario= request.user)
        form = FormTarea(request.POST, instance=tarea)
        form.save()
        return redirect('tareas')
    
def CompletarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario= request.user)
    if request.method == 'POST':
        tarea.completado = timezone.now()
        tarea.save()
        return redirect('tareas')
    
def EliminarTarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, usuario= request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect('tareas')
    

        