from django.shortcuts import render
# Create your views here.
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

@login_required(login_url='/momofit/login/') 
def Hello_momo(request):
    if request.user.is_authenticated:
        # print(request.user.kcal)
        context = {
            "name": request.user.username,
            "age": request.user.age,
            "sex": request.user.sex,
            "height": None,#request.user.height,
            "weight": None,#request.user.weight,
            "kcal": None#request.user.kcal 不在user裡面了換到history table裡
        }
    else:
        context = None
    return render(request, 'profile.html', context=context)