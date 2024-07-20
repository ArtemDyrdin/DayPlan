from django.shortcuts import render, redirect
from .forms import DayPlansForm, AuthUserForm, RegisterUserForm, LettersForm, Change_passwordForm
from .models import DayPlans

from django.views.generic import UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy, reverse
from django.http import HttpResponseForbidden


def main_page(request):
    data = {
        'title': 'Главная'
    }
    return render(request, 'dyplan/main_page.html', data)


def myplans(request):
    dt = DayPlans.objects.order_by('-date')
    data = {
        'title': 'Mои планы',
        'dt': dt
    }
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    return render(request, 'dyplan/myplans.html', data)


def dayplan(request):
    error = ''
    if request.method == 'POST':
        form = DayPlansForm(request.POST)
        if form.is_valid():
            object = form.save(commit=False)
            object.author = request.user
            object.save()
            return redirect('myplans')
        else:
            error = 'Ошибка формы'

    form = DayPlansForm()
    data = {
        'form': form,
        'title': 'План',
        'error': error
    }
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    return render(request, 'dyplan/dayplan.html', data)


def account(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = Change_passwordForm(request.POST)
        if form.is_valid():
            print('...\n', ' \n', 'OK\n', ' \n', '...')
            password = form.cleaned_data['password']
            request.user.set_password(password)
            request.user.save()
            auth_user = authenticate(username=request.user, password=password)
            login(request, auth_user)
            return redirect('account')
    else:
        form = Change_passwordForm()

    dt = {
        'title': 'Аккаунт',
        'form': form
    }
    return render(request, 'dyplan/account.html', dt)

#Edit, Delete (plans)


class PlanUpdate(LoginRequiredMixin, UpdateView):
    model = DayPlans
    template_name = 'dyplan/edit.html'
    form_class = DayPlansForm
    success_url = reverse_lazy('myplans')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self, **kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return handle_no_permission()
        return kwargs


def delete_plan(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    get_plan = DayPlans.objects.get(pk=pk)
    if request.user != get_plan.author:
        return HttpResponseForbidden()
    get_plan.delete()
    return redirect(reverse('myplans'))

#Registration, LogIn, delete (user), change_theme


def register(request):
    if request.user.is_authenticated:
        return HttpResponseForbidden()
    else:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()

                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                auth_user = authenticate(username=username, password=password)
                login(request, auth_user)
                return redirect('myplans')

        else:
            form = RegisterUserForm()

        dt = {
            'form': form,
        }

        return render(request, 'dyplan/signup.html', dt)


class LogInView(LoginView):
    template_name = 'dyplan/login.html'
    form_class = AuthUserForm
    success_url = '/myplans'


def contacts(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    else:
        error = 'Ошибка отправки формы'
        complete = 'Ваше сообщение успешно отправлено!'
        form = LettersForm()
        complete = ''
        data = {'form': form, 'complete': complete}

        if request.method == 'POST':
            form = LettersForm(request.POST)
            if form.is_valid():
                object = form.save(commit=False)
                object.author = request.user
                object.save()
                return redirect('contacts')

        return render(request, 'dyplan/contacts.html', {'form': form})


def delete_user(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    request.user.delete()
    return redirect('/')


def change_theme(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    if request.user.profile.theme == False:
        request.user.profile.theme = True
        request.user.profile.save()
    else:
        request.user.profile.theme = False
        request.user.profile.save()

    return redirect('account')
