from django.shortcuts import render,redirect
from .serializer import loginserializers
from .models import modellogin

# Create your views here.
def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if modellogin.objects.filter(username=username).exists():
            return render(request, 'register.html', {'errormessage': 'username already taken' })
        
        new_user = modellogin(username=username,password=password)
        new_user.save()
        
        request.session['user_id'] = new_user.id
        
        return redirect('home_page')
    
    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = modellogin.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                return redirect('home_page')
            else:
                return render(request, 'login.html', {'errormessage': 'invalid password'})
        except modellogin.DoesNotExist:
            return render(request, 'login.html', {'errormessage': 'user does not exist'})
        
    return render(request, 'login.html')
    
def home_page(request):
    return render(request, 'home.html')
    
def logout_page(request):
    request.session.pop('user_id', None)
    return render(request, 'login.html')