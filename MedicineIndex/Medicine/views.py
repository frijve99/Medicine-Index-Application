from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required #
from django.contrib.auth import authenticate, login,logout 
from django.contrib import messages
from .models import Medicine
from django.contrib.auth.models import User,auth
from django.db.models import Q


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
@login_required
def createAdmin(request):
    if request.user.is_superuser:
        if request.method=='POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
        
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
                    return redirect('viewAdmins')
            else:
                messages.info(request, 'Password dont match')
                return redirect('createAdmin')
        return render(request,'createAdmin.html')
    else:
        messages.info(request, 'You are not authorized to view this page!')
        return redirect('viewMedicines')

@login_required
def viewAdmins(request):
    if request.user.is_superuser:
        users = User.objects.exclude(is_superuser=True)
        context = {
            'users': users
        }
        return render(request, 'viewAdmins.html', context)
    messages.info(request, 'You are not authorized to view this page!')
    return redirect('viewMedicines')
    
@login_required
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
    isAdmin = 'False'
    #check if super use
    if request.user.is_authenticated:
        isAdmin = 'True'
    context = {
        'isAdmin': isAdmin
    }
    return render(request, 'addMedicines.html', context)


def highlight_text(text, keyword):
    if keyword:
        keyword = keyword.lower()
        highlighted_text = ''
        index  = text.lower().find(keyword)
        
        highlighted_text += text[:max(index - 1,0)] 
        highlighted_text += f'<span class="highlight">{text[index:index + len(keyword)] }</span>' 
        highlighted_text += text[(index + len(keyword)):]
        print(index)
        print(highlighted_text)
        return highlighted_text
        
    return text

def viewMedicines(request):
    queryKeyword = request.GET.get('search', '')
    if queryKeyword:
        medicines = Medicine.objects.filter(Q(name__icontains=queryKeyword) | Q(generic_name__icontains=queryKeyword))
        for medicine in medicines:
            medicine.name = highlight_text(medicine.name, queryKeyword)
            medicine.generic_name = highlight_text(medicine.generic_name, queryKeyword)

    else:
        medicines = Medicine.objects.all()

    isAdmin = 'False'
    if request.user.is_authenticated:
        isAdmin = 'True'

    context = {
        'medicines': medicines,
        'isAdmin': isAdmin,
        'queryKeyword': queryKeyword
    }

    return render(request, 'viewMedicines.html', context)


def medicineDetails(request, pk):
    medicine = Medicine.objects.get(id=pk)
    isAdmin = 'False'

    if request.user.is_authenticated:
        isAdmin = 'True'
    context = {
        'medicine': medicine,
        'isAdmin': isAdmin
    }
    return render(request, 'medicineDetails.html', context)

def index(request):
    medicines = Medicine.objects.all()
    return render(request, 'index.html')

def search(request):
    return render(request, 'index.html')


@login_required
def editMedicine(request, pk):
    
    if request.method == 'POST':
        medicine_name = request.POST.get('medicineName')
        generic_name = request.POST.get('genericName')
        manufacturer = request.POST.get('manufacturer')
        description = request.POST.get('description')
        price = request.POST.get('price')
        batch_number = request.POST.get('batch_number')
        
        medicine_obj = Medicine.objects.get(id=pk)
        medicine_obj.name = medicine_name
        medicine_obj.generic_name = generic_name
        medicine_obj.manufacturer = manufacturer
        medicine_obj.description = description
        medicine_obj.price = price
        medicine_obj.batch_number = batch_number
        medicine_obj.save()
        messages.success(request, 'Medicine updated successfully!')
        return redirect('medicineDetails', pk=pk)

    medicine = Medicine.objects.get(id=pk)
    isAdmin = 'False'

    if request.user.is_authenticated:
        isAdmin = 'True'
    context = {
        'medicine': medicine,
        'isAdmin': isAdmin
    }
    return render(request, 'editMedicine.html', context)
    
@login_required
def deleteMedicine(request, pk):

    # if request.method == 'POST':
    #     medicine_obj = Medicine.objects.get(id=pk)
    #     medicine_obj.delete()
    #     messages.success(request, 'Medicine deleted successfully!')
    #     return redirect('viewMedicines')
    print("Delete Medicine")
    medicine = Medicine.objects.get(id=pk)
    medicine.delete()
    return redirect('viewMedicines')
@login_required
def logout(request):
    auth.logout(request)
    return redirect('index')

@login_required
def deleteAdmin(request, pk):
    user = User.objects.get(username=pk)
    user.delete()
    return redirect('viewAdmins')
@login_required
def editAdmin(request, pk):
    if request.method == 'POST':
        newEmail = request.POST.get('email')

        if User.objects.filter(email=newEmail).exists():
                messages.info(request, 'Email Taken')
                return redirect('editAdmin')
        
        user = User.objects.get(username=pk)
        user.email = newEmail
        user.save()
        messages.success(request, 'Admin updated successfully!')
        return redirect('viewAdmins')
    user = User.objects.get(username=pk)
    context = {
        'user': user
    }
    return render(request, 'editAdmin.html', context)