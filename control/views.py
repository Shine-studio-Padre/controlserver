import shutil

from django.shortcuts import render, redirect, render_to_response
import os
# Create your views here.
from control.forms import CheckoutContactForm
from control.models import *
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
def index(request):
    userfunc = {
        'user': auth.get_user(request).username,
        'func_user': UserFunction.objects.all()
    }
    return render(request, 'server/index.html', userfunc)


def account(request):
    global aff
    new_file = request.POST.get('new_file', 'none')
    del_file = request.POST.get('del_file', 'none')
    del_file_file = request.POST.get('del_file_file', 'none')
    write_file = request.POST.get('write_file', 'none')
    new_doc = request.POST.get('new_doc', 'none')
    list_dir = request.POST.get('list_dir', 'none')
    try:
        def write():
            if del_file_file != 'none':
                f = open("c:/test/%s/%s" % (auth.get_user(request).username, del_file_file))
                a = f.read()
                f.close()
                return a

        aga = os.listdir(path="c:/test/%s/ad"% auth.get_user(request).username)
        print(aga)
    except Exception:
        print("Чтение файлов - отсутствует")
    try:
        if del_file_file == 'none':
            print('')
        else:
            aff = del_file_file
        if aff != 'none':
            if write_file != 'none':
                f = open("c:/test/%s/%s" % (auth.get_user(request).username, aff), 'w+')
                print(write_file)
                f.write(write_file)
                f.close()
    except Exception:
        print("Редактирование файлов - отсутствует")
    try:
            os.mkdir("c:/test/%s/%s" % (auth.get_user(request).username, new_file))
    except Exception:
        print("Добавление папок - отсутствует")
    try:
        cc = open("c:/test/%s/%s" % (auth.get_user(request).username, new_doc), 'w+')
        cc.close()
    except Exception:
        print("Добавление файлов - отсутствует")
    if del_file_file != 'none':
        f = open("c:/test/%s/%s" % (auth.get_user(request).username, del_file_file))
        a = f.read()
    file_s = os.listdir(path="c:/test/%s" % auth.get_user(request).username)
    try:
        open_list = os.listdir(path="c:/test/%s/%s" % (auth.get_user(request).username, list_dir))
        print(open_list)
    except Exception:
        print("Добавление файлов - отсутствует")
    userfunc = {
        'user': auth.get_user(request).username,
        'func_user': UserFunction.objects.all(),
        'file_s': file_s,
        'open_file': write(),
        'open_list': open_list,
        'list_dir':  list_dir

    }

    return render(request, 'server/account.html', userfunc)

def login(request):
    if request.POST:
        username = request.POST.get('username', 'fgdg')
        password = request.POST.get('password', 'ergerg')
        print(password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/account')
        else:
            login_error = "Netu tebia"

    return render(request, 'server/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def register(request):
    username = request.POST.get('username', 'none')
    password = request.POST.get('password', 'none')
    email = request.POST.get('mail', 'none')
    name = request.POST.get('name', 'none')

    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password = newuser_form.cleaned_data['password2'], is_active = False)
            try:
                os.mkdir("c:/test/%s" % newuser)
            except:
                return redirect("/")
            auth.login(request, newuser)
            return redirect('/account')
        else:
            args['form']=newuser_form
    return render(request, 'server/registration.html', args)
