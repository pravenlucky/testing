from django.contrib import auth
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
# from django.contrib.auth.forms import UserCreationForm
from inventory.forms import MyRegistrationForm, EditProfileForm


def register_view(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registered/')

    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    args['user'] = request.user
    return render_to_response('register.html', args)


def registered_view(request):
    return render_to_response('registered.html', {'user': request.user})


def login_view(request):
    c = {}
    c.update(csrf(request))
    c['user'] = request.user
    return render_to_response('login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/logged_in')
    else:
        return HttpResponseRedirect('/invalid')


def logged_in_view(request):
    name = request.user.username
    return render_to_response('logged_in.html', {'name': name, 'user': request.user})


def logout_view(request):
    auth.logout(request)
    return render_to_response('logout.html')


def invalid_view():
    return render_to_response('invalid.html')


def edit_profile(request):
    #profile = request.user.get_profile()
    edit_profile_form = EditProfileForm(request.POST)
    #\ or None,current_user=request.user)#, instance=profile)

    if request.method == 'POST':
        if edit_profile_form.is_valid():
            edit_profile_form.save()
            return HttpResponseRedirect('/articles/all')

    #context = {'edit_profile_form': edit_profile_form}
    #return render(request, '/edit_profile.html', context)
    else:
        f = EditProfileForm()
        args = {}
        args.update(csrf(request))
        args['form'] = f
        args['user'] = request.user
        return render_to_response('edit_profile.html', args)