from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contacts.models import Contact
from django.contrib.auth.models import User

# Create your views here.

def register(request):

  if request.method == 'POST':
    #  Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Check if passwords match
    if password == password2:

      # Check username
      if User.objects.filter(username = username).exists():
        messages.error(request, 'Username already exists!')
        return redirect('register')
      else:

        # Check email
        if User.objects.filter(email = email).exists():
          messages.error(request, 'Email already exists!')
          return redirect('register')
        else:
          # Looks good
          user  = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)

          # Log user in. Method 1
          """ auth.login(request, user)
          messages.success(request, "You're now logged!")
          return redirect('index') """

          # Log user in. Method 2
          user.save()
          messages.success(request, "You're registered. You can now log in")
          return redirect('login')

    else:
      messages.error(request, 'Passwords do not match')
      return redirect('register')
  else:
   return render(request, 'accounts/register.html')

def login(request):

  if request.method == 'POST':
    # Login user in. Method 2 continue
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, "you're now logged in!")
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid credentials!')
      return redirect('login')
  else:
   return render(request, 'accounts/login.html')

def logout(request):
 if request.method == 'POST':
   auth.logout(request)
   messages.success(request, "You're now logged out")
   return redirect('index')
  
def dashboard(request):
  # View listings in dashboard
  user_id = request.user.id
  user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=user_id)

  context = {
    'contacts' : user_contacts
  }

  return render(request, 'accounts/dashboard.html', context)