from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required #
from django.contrib.auth import authenticate, login,logout 
from django.contrib import messages
from .models import Medicine
from django.contrib.auth.models import User,auth


def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid User')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def createAdmin(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # print("ELLO")
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                user= User.objects.filter(email=email).first()
                user_profile = User.objects.filter(email=email).first()
                messages.info(request, 'Email Taken')
                return redirect('createAdmin')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('createAdmin')
            else:
                user = User.objects.create_user(username=username,password=password, email=email)
                user.save()
                messages.info(request,'An Admin has been Created...')               
                return redirect('createAdmin')
        else:
            messages.info(request, 'Password dont match')
            return redirect('createAdmin')
    else:
        return render(request,'createAdmin.html')

def viewAdmins(request):
    return render(request, 'viewAdmins.html')

def addMedicines(request):
    if request.method == 'POST':
        # Retrieve the data from the request
        medicine_name = request.POST.get('medicineName')
        generic_name = request.POST.get('genericName')
        manufacturer = request.POST.get('manufacturer')
        description = request.POST.get('description')
        price = request.POST.get('price')
        batch_number = request.POST.get('batch_number')
        #print(medicine_name, generic_name, manufacturer, description, price, batch_number)
        if Medicine.objects.filter(name=medicine_name).exists():
            messages.error(request, 'Medicine with this name already exists!')
            return redirect('addMedicines')
        medicine_obj = Medicine(name=medicine_name, generic_name=generic_name, manufacturer=manufacturer, description=description, price=price, batch_number=batch_number)
        medicine_obj.save()
        messages.success(request, 'Medicine added successfully!')
        return redirect('viewMedicines')
    return render(request, 'addMedicines.html')

def viewMedicines(request):
    medicines = Medicine.objects.all()

    isAdmin = 'False'

    if request.user.is_authenticated:
        isAdmin = 'True'

    context = {
        'medicines': medicines,
        'isAdmin': isAdmin
    }

    return render(request, 'viewMedicines.html', context)


def medicineDetails(request, pk):
    medicine = Medicine.objects.get(id=pk)
    context = {
        'medicine': medicine
    }
    return render(request, 'medicineDetails.html', context)

@login_required
def index(request):
    medicines = Medicine.objects.all()
    return render(request, 'index.html')

def search(request):
    return render(request, 'index.html')

def medicine_detail(request, pk):
    return render(request, 'index.html')

def medicine_create(request):
    return render(request, 'index.html')

def medicine_edit(request, pk):
    return render(request, 'index.html')

def medicine_delete(request, pk):
    return render(request, 'index.html')
