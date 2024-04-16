from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.db import IntegrityError

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        mail = request.POST.get('mail')
        #Chequea que el correo electronico no este en uso
        if User.objects.filter(mail=mail).exists():
            return JsonResponse({'message': 'El correo electronico ya esta en uso'}, status=400)
        #Chequea que el nombre de usuario no este en uso
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'El nombre de usuario ya esta en uso'}, status=400)
        #Registra el usuario en la base de datos
        try:
            User.objects.create(username=username, password=password, name=name, last_name=last_name, mail=mail)
            return JsonResponse({'message': 'Usuario registrado exitosamente'})
        except IntegrityError as e:
            return JsonResponse({'message': 'Error al registrar el usuario'}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).exists()
        if user:
            return JsonResponse({'message': 'Inicio de sesion exitoso'})
        else:
            return JsonResponse({'message': 'Nombre de usuario o contraseña incorrectos'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

def register_form(request):
    return render(request, 'register.html')

def login_form(request):
    return render(request, 'login.html')
