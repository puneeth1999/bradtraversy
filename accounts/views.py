from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from contacts.models import Contact
# Create your views here.

def register(request):
    if request.method == "POST":
        # Register User
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Check if passwords match
        if password == password2:
            # Check Username
            if User.objects.filter(username = username).exists():
                messages.error(request, "Username is unavailable")
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, "Account already exists with this e-mail address")
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username = username, password=password, email=email, first_name = first_name, last_name = last_name)
                    # Login after registration
                    # auth.login(request, user)
                    # messages.success(request, 'You\'re logged in')
                    
                    #Manually login
                    user.save()
                    messages.success(request,'You\'re registered and can login')
                    return redirect('login')
                
        else:
            messages.error(request, 'Passwords do not match')

        return redirect('register')
    return render(request, 'accounts/register.html', context={})
    

def login(request):
    
    if request.method == "POST":
        # Login User
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')   
    return render(request, 'accounts/login.html', context={})

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You're logged out")
        return redirect('index')
