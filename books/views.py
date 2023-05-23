from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from books.forms import*
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import json
import razorpay
import random
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

def order_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        orderid=request.POST.get("provider_order_id")
        issueid=request.POST.get("issueid")
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": float(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Ordernow.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order['id'],issueid_id=issueid
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "callback_url": "http://127.0.0.1:8000/callback/",
                "razorpay_key": settings.RAZORPAY_KEY_ID,
                "order": order,
            },
        )
    return render(request, "payment.html")


@csrf_exempt
def callback(request):
    
    razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    #    return client.utility.verify_payment_signature(response_data)

    if request.method == "POST":
        try:
            payment_id = request.POST.get("razorpay_payment_id", "")
            provider_order_id = request.POST.get("razorpay_order_id", "")
            signature_id = request.POST.get("razorpay_signature", "")
            params_dict={
                'razorpay_order_id':provider_order_id,
                'razorpay_payment_id':payment_id,
                'razorpay_signature':signature_id

            }
            print(params_dict)
            try:
                order = Ordernow.objects.get(provider_order_id=provider_order_id)
            except:
                return HttpResponse("505 not found inner")
            order.payment_id = payment_id
            order.signature_id = signature_id
            order.save()
            
            result=razorpay_client.utility.verify_payment_signature(params_dict)
            
            if result==True:
                amount=int(order.amount)
                
                try:
                   
                    '''res=razorpay_client.payment.capture(payment_id,{
                        "amount" : amount,
                        "currency" : "INR"
                        })
                    print(res)'''
                    order.status=PaymentStatus.SUCCESS
                    order.save()
                    return render(request, "sucess.html")
                except:
                   
                    order.status=PaymentStatus.FAILURE
                    order.save()
                    return render(request, "failure.html")
            else:
                
                order.status=PaymentStatus.FAILURE
                order.save()
                return render(request, "failure.html")
        except:
            return HttpResponse("505 not found here")
        

#create your views here.

def homeview(request):
    blg=blog.objects.all()[0:4]
    return render(request,"home.html",{'blg':blg})

def Aboutview(request):
    services=service.objects.all()
    return render(request,"About.html",{'services':services})

def faqview(request):
    faqs=faq.objects.all()
    return render(request,"faq.html",{'faqs':faqs})

def categoryview(request,id):
    books=book.objects.filter(categoryid_id=id)
    return render(request,"category.html",{'books':books})

class spacesview(TemplateView):
    template_name="spaces.html"

class blogdetailview(TemplateView):
    template_name="blog.html"

class contactview(TemplateView):
    template_name="contact.html"

def dashboardview(request):
    userid=request.user.id
    issues=issuebook.objects.filter(username_id=userid,status='Issued').count()
    returns=issuebook.objects.filter(username=userid,status='Returned').count()
    context={'issues':issues,'returns':returns}
    return render(request,"dashboard.html",context)

def issuedbooksview(request):
    userid=request.user.id
    issueb=issuebook.objects.filter(username_id=userid,status='Issued')
    return render(request,"issuedbooks.html",{'issueb':issueb}) 


'''def returnedbooksview(request):
    userid=request.user.id
    #issueba=issuebook.objects.filter(username_id=userid,status='Returned')
    issueb=Ordernow.objects.select_related('issueid').filter(issueid__username_id=userid,issueid__status='Returned')
    if not issueb:
        issueba=issuebook.objects.filter(username_id=userid,status='Returned')
        context={'issueba':issueba}
    else:
        context={'issueb':issueb}
    return render(request,"returnedbooks.html",context) '''

def returnedbooksview(request):
    userid=request.user.id
    #issueba=issuebook.objects.filter(username_id=userid,status='Returned')
    issueba=issuebook.objects.filter(username_id=userid,status='Returned')
    context={'issueba':issueba}

        
    return render(request,"returnedbooks.html",context)    

def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/')
    else:
        form=contactform()
    return render(request, "contact.html",{'form':form})

def insertsubscribe(request):
    if request.method=='POST':
        form=subscribeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form=subscribeform()
    return render(request, "home.html",{'form':form}) 

def blogview(request):
    blg=blog.objects.all()
    return render(request,"home.html",{'blg':blg})

def blogdetailview(request,id):
    b=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'b':b})

def blogview1(request):
    blg=blog.objects.all()
    return render(request,"Blogs.html",{'blg':blg})


def Ourbooksview(request):
    categorys=category.objects.all()
    return render(request,"Ourbooks.html",{'categorys':categorys})


def signup(request):
    next=""
    if request.GET:
        next=request.GET['next']
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,User)
            if next=="":
                return redirect('/dashboard/')
            else:
                return redirect(next)
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})


def loginuser(request):
    next=""
    if request.GET:
        next=request.GET['next']
    print(next)
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request,user)
            if next=="":
                return redirect('/dashboard/')
            else:
                return redirect(next)

        
def categorydetailview(request,id):
    categorys=book.objects.get(id=id)
    return render(request,"categorydetail.html",{'categorys':categorys})


def issuedview(request,id):
    b=book.objects.get(id=id)
    return render(request,"issued.html",{'b':b})

def insertbook(request):
    if request.method=='POST':
        form=issuedform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/issuedbooks/')
    else:
        form=issuedform()
    return render(request, "issued.html",{'form':form})

def returnview(request,id):
    r=issuebook.objects.get(id=id)
    return render(request,'return.html',{'r':r})

def updatereturn(request,id):
    r=issuebook.objects.get(id=id)
    form=issuedform(request.POST,instance=r)
    if form.is_valid():
        form.save()
        return redirect('/dashboard/')
    return render(request,'return.html',{'form':form})