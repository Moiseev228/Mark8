from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import redirect
from administration_app.models import Staff

def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['login'] = username
            type_user = Staff.objects.get(login_employee=username).type_users
            if type_user == 'administration':
                return redirect('../administration/main')
            elif type_user == 'registry':
                return redirect('../registry/main')
            elif type_user == 'medico':
                return redirect('../extract/main')
            else:
                args['login_error'] = 'Недопустим тип пользователя. Обратитесь в службу потдержки'
                return render(request, 'logsys/login.html', args)
        else:
            args['login_error'] = 'Пользователь не найден'
            return render(request, 'logsys/login.html', args)
    else:
        return render(request, 'logsys/login.html', args)
    

def logout(request):
    auth.logout(request)
    return redirect('http://127.0.0.1:8000/logsys/login')