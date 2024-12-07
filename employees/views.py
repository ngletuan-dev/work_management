from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Employee, CheckInOut, Shift
from django.utils import timezone

@login_required
def check_in(request):
    employee = Employee.objects.get(user=request.user)
    check_in_record = CheckInOut.objects.create(employee=employee, check_in_time=timezone.now())
    return redirect('shifts')  # Chuyển hướng về trang chủ sau khi check-in

@login_required
def check_out(request):
    employee = Employee.objects.get(user=request.user)
    check_in_record = CheckInOut.objects.filter(employee=employee, check_out_time__isnull=True).latest('check_in_time')
    check_in_record.check_out_time = timezone.now()
    check_in_record.save()
    return redirect('shifts')  # Chuyển hướng về trang chủ sau khi check-out

@login_required
def shifts(request):
    shifts = Shift.objects.all()
    return render(request, 'employees/shifts.html', {'shifts': shifts})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('shifts')  # Chuyển hướng tới trang chủ sau khi đăng nhập thành công
        else:
            error_message = 'Invalid login credentials'
            return render(request, 'employees/login.html', {'error_message': error_message})
    return render(request, 'employees/login.html')
