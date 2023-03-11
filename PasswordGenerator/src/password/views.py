from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def passwords(request):

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0987654321"
    symbols = "!@#$%&*?"

    to_generate = lower_case + upper_case + numbers + symbols

    length_password = int(request.GET.get('number_characters'))

    password = "".join(random.sample(to_generate, length_password))


    return render(request, 'password.html', {"passwords": password})