from django.shortcuts import render, get_object_or_404, redirect
from .models import Phone, CostomOption, PhoneSold, Repository
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import BuyPhoneForm, SignupForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
    num_phones = Phone.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_phones': num_phones, 'num_visits': num_visits}, )


@login_required
def phonesold(request):
    phonesold = PhoneSold.objects.filter(buyer=request.user)
    return render(request, 'catalog/phonesold.html', {'phonesold': phonesold})


@login_required
def phone_buy(request, pk):
    repository = get_object_or_404(Repository, phone=pk)
    phone = get_object_or_404(Phone, pk=pk)
    if request.method == "POST":
        form = BuyPhoneForm(request.POST)
        if form.is_valid():
            phonesold = form.save(commit=False)
            phonesold.buyer = request.user
            phonesold.time_of_purchase = timezone.now()
            phonesold.product = phone.name
            phonesold.save()
            return redirect('payment', pk=repository.pk)
    else:
        form = BuyPhoneForm()
    return render(request, 'catalog/phone_buy.html', {'form': form})


def phone_list(request):
    phones = Phone.objects.all()
    paginator = Paginator(phones, 10)

    page = request.GET.get('page')
    try:
        phones = paginator.page(page)
    except PageNotAnInteger:
        phones = paginator.page(1)
    except EmptyPage:
        phones = paginator.page(paginator.num_pages)
    return render(request, 'catalog/phone_list.html', {'phones': phones})


def phone_detail(request, pk):
    phone = get_object_or_404(Phone, pk=pk)
    ava = get_object_or_404(Repository, phone=pk)
    if ava.numbers > 0:
        ava.status = 'a'
        ava.save()
    return render(request, 'catalog/phone_detail.html', {'phone': phone})


def costomoption_list(request):
    costomoptions = Phone.objects.all()
    return render(request, 'catalog/costomoption_list.html', {'costomoptions': costomoptions})


def costomoption_detail(request, pk):
    costomoption = get_object_or_404(CostomOption, pk=pk)
    return render(request, 'catalog/costomoption_detail.html', {'costomoption': costomoption})


@login_required
def payment(request, pk):
    repository = get_object_or_404(Repository, phone=pk)
    phone = get_object_or_404(Phone, pk=pk)
    time_of_purchase = timezone.now()
    user = request.user
    email = user.email
    if repository.numbers > 1:
        repository.numbers -= 1
    elif repository.numbers == 1:
        repository.numbers -= 1
        repository.status = 'u'
    else:
        repository.status = 'u'
    repository.save()
    number = repository.numbers
    return render(request, 'catalog/payment.html', {'number': number, 'repository': repository, 'phone': phone, 'time_of_purchase': time_of_purchase, 'user': user, 'email': email, })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form.cleaned_data)
            return redirect('signupsuccess')
    else:
        form = SignupForm()

    return render(request, 'catalog/signup.html', {'form': form})


def signupsuccess(request):
    return render(request, 'catalog/signup_success.html', {})
