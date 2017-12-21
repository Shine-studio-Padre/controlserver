from django.shortcuts import render

# Create your views here.
from django.template.context_processors import csrf
from control.models import *
from django.contrib import auth
from django.shortcuts import render_to_response, redirect

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', 'fgdg')
        password = request.POST.get('password', 'ergerg')
        print(password)
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Pol'zovatel' ne naiden"
            return render_to_response('server/login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

