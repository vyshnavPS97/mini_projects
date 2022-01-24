from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import client, place_order, payment_details, juice


def index(request):
    return render(request, 'pages/index.html')

def logins(request):
    return render(request, 'pages/login.html')
def placeorder(request):
    return render(request, 'pages/placeorder.html')
def registers(request):
    return render(request, 'pages/register.html')
def home(request):
    return render(request, 'pages/home.html')
def payment(request):
    return render(request, 'pages/payment.html')
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('uname')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        try:
            a = client(cli_email=email, cli_name=name, cli_contact=contact, cli_password=password )
            a.save()
            mes = "successfuly registered"
            return render(request, 'pages/register.html', {'mes':mes})
        except:
            req = "enter required field"
            return render(request, 'pages/register.html', {'req':req})
    else:
        return render(request, 'pages/register.html')

def signin(request):
    if request.method == "POST":
        if client.objects.filter(cli_email=request.POST['email'], cli_password=request.POST['password']).exists():
            b = client.objects.get(cli_email=request.POST['email'], cli_password=request.POST['password'])
            return render(request, 'pages/home.html', {'client':b})
        else:
            c = "invalid username or password"
            return render(request, 'pages/login.html', {'invalid':c})
    else:
        return render(request, 'pages/login.html')
def logout(request):
    return render(request, 'pages/login.html')
def myorder(request):
    return render(request, 'pages/myorders.html')

def order(request):
    if request.method == "POST":
        itemname = request.POST.get('itemname')
        itemcount = request.POST.get('itemcount')
        location = request.POST.get('location')
        contact = request.POST.get('contact')
        try:
            a = place_order(item_name=itemname, item_count=itemcount, item_location=location, item_contact=contact)
            a.save()
            ferroro = 95
            amount = int(itemcount)* ferroro
            return render(request, 'pages/payment.html', {'amount':amount})
        except:
            return render(request, 'pages/placeorder.html')
    else:
        return render(request, 'pages/placeorder.html')

def payed(request):
    if request.method == "POST":
        cardnumber = request.POST.get('cardnumber')
        exmonth = request.POST.get('month')
        exyear = request.POST.get('year')
        cvv = request.POST.get('cvv')
        try:
            a = payment_details(card_number=cardnumber, expiry_month=exmonth, expiry_year=exyear, cvv=cvv)
            a.save()
            success = "your order is placed"
            return render(request, 'pages/payment.html',{'mes':success})
        except:
            return render(request, 'pages/payment.html')
    else:
        return render(request, 'pages/payment.html')

def show_order_details(request):
    list = place_order.objects.all()
    return render(request, 'pages/myorders.html', {'list':list})

def delete(request, item_id):
    a = place_order.objects.get(item_id=item_id)
    a.delete()
    return redirect('/myapp/show')
def edit(request, item_id):
    a = place_order.objects.get(item_id=item_id)
    return render(request,'pages/edit.html', {'a':a})

def update(request, item_id):
    a = place_order.objects.get(item_id=item_id)
    a.item_name = request.POST.get('itemname')
    a.item_count = request.POST.get('itemcount')
    a.item_location = request.POST.get('location')
    a.item_contact = request.POST.get('contact')
    a.save()
    return redirect('/myapp/show')

def search(request):
    if request.method == "POST":
        searched = request.POST.get('search')
        it = place_order.objects.filter(item_location__icontains= searched)
        return render(request, 'pages/myorders.html', {'searched_item': it})
    else:
        return render(request, 'pages/myorders.html')


def aboutus(request):
    return render(request, 'pages/about.html')
def drinks(request):
    drinkss = juice.objects.all()
    return render(request, 'pages/drinks.html', {'drinks':drinkss})
