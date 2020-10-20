from django.shortcuts import render, reverse
from django_tables2 import RequestConfig
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cities.models import City, Continent
from cities.tables import CityTable
from cities.forms import SignupForm, LoginForm


@login_required(login_url='/login/')
def city_list(request):
    """
    The Controller prepares tables for displaying a list of cities as tables.
    For authorized users only.
    :param request: HttpRequest object
    :return: HttpResponse object returned as a result of calling render()
    function with passed arguments (html document with city tables)
    """

    config = RequestConfig(request)
    continents = Continent.objects.all().order_by('name')
    tables = [CityTable(City.objects.filter(continent=continent),
                        prefix=continent.name) for continent in continents]

    for table in tables:
        config.configure(table)

    return render(request, 'cities/city_list.html', {
        'tables': tables,
    })


def sign_up(request):
    """
    The Controller is responsible for registering and authenticating the user
    in the system. Logs in the user on successful authentication.
    :param request: HttpRequest object
    :return: HttpResponse object returned as a result of calling render()
    function with passed arguments (html document with registration form);
    Redirecting to a page with city tables on successful registration and
    authentication, or returning an HttpResopnse object with a 400 status code.
    """

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form.save()
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('cities'))
            else:
                return HttpResponseBadRequest()
    else:
        form = SignupForm()

    return render(request, 'cities/signup_form.html', {
        'form': form,
    })


def log_in(request):
    """
    The Controller is responsible for authentication and user login in the
    system.
    :param request: HttpRequest object
    :return: HttpResponse object returned as a result of calling render()
    function with passed arguments (html document with login form);
    Redirecting to a page with city tables on successful authentication,
    or returning an HttpResopnse object with a 400 status code
    """

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('cities'))
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль')
    else:
        form = LoginForm()

    return render(request, 'cities/login_form.html', {
        'form': form,
    })


def log_out(request):
    """
    The Controller is responsible for user logout.
    :param request: HttpRequest object
    :return: Redirect to login page
    """

    if request.user is not None:
        logout(request)
        return HttpResponseRedirect(reverse('login'))
