from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView

from accountapp.forms import CustomUserCreationForm
from accountapp.models import CustomUser


# Create your views here.

def main(request):
    if request.user.is_authenticated:
        return render(request, 'accountapp/main.html')
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accountapp:main')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = CustomUser
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'