from django.shortcuts import render, redirect

from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, FormView, RedirectView
from accounts.forms import *
from accounts.models import User

# Create your views here.
class RegisterEmployeeView(CreateView):
    """docstring for RegisterEmpoyeeView."""
    model = User
    form_class = EmployeeRegistrationForm
    template_name = 'accounts/employee/register.html'
    success_url = '/'

    extra_context = {
        'title':'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)
        super(RegisterEmpoyeeView, self).__init__()
        self.arg = arg
    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            return render(request, 'accounts/employee/register.html', {'form':form})

class RegisterEmployerView(CreateView):
    """docstring for RegisterEmployerView."""
    model = User
    form_class = EmployerRegistration
    template_name = 'accounts/employer/register.html'
    success_url = '/'

    extra_context = {
        'title':'Register'
    }
    def dispatch(self,request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def post(self, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()

            return redirect('accounts:login')

        else:
            return render(request, 'accounts/employer/register.html',{'form':form})

class LoginView(FormView):
    """docstring for LoginView."""
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title':'Login'
    }
    def dispatch(self,request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next']!='':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(RedirectView):
    """docstring for LogoutView."""

    url = '/login'

    def get(self,request, *args,**kwargs):
        auth.logout(request)
        message.success(request, 'You are now logging out')
        return super(LogoutView, self.get(request, *args, **kwargs))
