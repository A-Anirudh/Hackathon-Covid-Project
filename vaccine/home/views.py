from django.shortcuts import render, redirect
from .forms import *
import requests
import datetime
import hashlib

def home(request):

    if request.method == 'POST':
        form = VaccineCheckForm(request.POST)
        if form.is_valid():
            pin = form.cleaned_data['pin']
            vaccine_name = form.cleaned_data['vaccine_name']
            date  = form.cleaned_data['date'].strftime('%d-%m-%Y')
            base_url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={date}'
            data = requests.get(base_url).json()
            request.session['data'] = data
            return redirect('details')
    else:
        form = VaccineCheckForm()
    context={
        'form': form
    }
    return render(request, 'home/main.html', context=context)

def details(request):
    data = request.session.get('data')
    context={
        'data': data
    }
    return render(request, 'home/detail.html', context=context)


def verify(request):
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            mobile = form.cleaned_data['mobile']
            data = {
                'mobile': str(mobile),
                'secret': 'Vaccine@2020'
            }
            headers = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
            }

            url = 'https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP'
            data = requests.post(url, data=data, headers=headers)

            print(data)
    else:
        form = VerifyForm()
    context={
        'form': form
    }
    return render(request, 'home/verify.html', context=context)

