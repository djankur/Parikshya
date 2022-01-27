import email
from unicodedata import name
from django.core import paginator
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from datetime import *
from django.http import request, response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from Examapp.models import Registration
from django.contrib.auth import authenticate , login
from Examapp.models import *
from django.core.paginator import EmptyPage, InvalidPage, Paginator

lst=[]
anslst=[]
corans=Question.objects.all()

for i in  corans:
    anslst.append(i.correctans)

# Create your views here.
def home(req):
    return render(req,'home.html')
def regform(request):
    if request.method =="POST":
        name=request.POST['name']
        address=request.POST['address']
        pin=request.POST['pin']
        email=request.POST['email']
        phone=request.POST['phone']
        password= request.POST['password']
        # pwd=make_password(password)
        # hashed_password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        reg=Registration(name=name,address=address,pin=pin,email=email,phone=phone,password=password,date=datetime.today())
        reg.save()
        # return HttpResponse("datasaved")
        return render(request,'stdlogin.html')
        # print(user)
    else:
        return render(request,'regform1.html')

def stdlogin(request):
    lst.clear()
    if request.method == 'POST':
        email=request.POST['email']
        password =request.POST['password']
        request.session['email']=email
     
        try:
            std= Registration.objects.get(email=email,password=password)
            
            # name = Registration.objects.filter(email='email').values('name')
            print(std.name)
            # name = std.name
            # if not check_password(password,c.password):
            # return redirect('sindex')
            return render(request,'sindex.html',{"name":std.name})
            #  Registration.objects.get(email=email,password=pwd)
             
            
        except ObjectDoesNotExist:
            messages.warning(request, 'Wrong email or password !')
            print("Wrong email or password !")
            return redirect('stdlogin')
            #  print("wrong email password")
            # bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())
             
               
            # return redirect('question.html')
    else:
        return render(request,'stdlogin.html')

def sindex(requset):
    print('Session email : ',requset.session.get('email'))
    return render(requset,'sindex.html')
def qn(request):
    
    qus = Question.objects.all()
    paginator = Paginator(qus,1)

    try:
        page= int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        questions=paginator.page(page)
    except(EmptyPage,InvalidPage):
        questions=paginator.page(paginator.num_pages)
        

    return render(request,"index.html",{"qus":qus,'questions':questions})
    

def tindex(request):
    # if request.method=='GET':
    #     subname=request.GET.get('subname')
    #     eqty=request.GET.get('eqty')
    #     print(subname,"qnty:",eqty)
    #     eq = int(eqty)
    #     for i in range(eq):
    #         i=i-1
    #         return render(request,'question.html',{"eqty":eqty})
            
    # else:
    return render(request,'tindex.html')


def tealogin(request):
    if request.method == 'POST':
        username=request.POST['username']
        password =request.POST['password']
       
     
        try:
            Teacher.objects.get(username=username,password=password)
            
            # if not check_password(password,c.password):
            return render(request,'tindex.html')
            #  Registration.objects.get(email=email,password=pwd)
             
            
        except ObjectDoesNotExist:
            messages.warning(request, 'Wrong email or password !')
            print("Wrong email or password !")
            return redirect('tealogin')
            #  print("wrong email password")
            # bcrypt.checkpw(request.POST['password'].encode(), user.password.encode())
             
               
            # return redirect('question.html')
    else:
        return render(request,'tealogin.html')

def logout(request):
    return redirect('tealogin')



def addqn(request):


    if request.method =="POST":
        qnid=request.POST['qid']
        question=request.POST['question']
        option1=request.POST['option1']
        option2=request.POST['option2']
        option3=request.POST['option3']
        option4=request.POST['option4']
        correctans= request.POST['correctans']
        # pwd=make_password(password)
        # hashed_password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        qn=Question(qid=qnid,question=question,option1=option1,option2=option2,option3=option3,option4=option4,correctans=correctans)
        qn.save()
        # return HttpResponse("datasaved")
        return render(request,'question.html')
        # print(user)
    else:
        
        return render(request,'question.html')


def viewqn(request):
    # if request.method == "POST":
    #     qid=request.POST.get('qid')
    #     qd=request.POST['qn']
    #     Question.objects.filter(qid=qid).update(question=qd)
    
    #     return HttpResponse("updated")
    # else:   
        qn = Question.objects.all()
        return render(request,'viewqn.html',{"qn":qn})
    # return render(request,'viewqn.html')


def delete(request):
    if request.method == "POST":
        qid=request.POST.get('qid')
        
        Question.objects.filter(qid=qid).delete()
    
        return HttpResponse("delete")
    else:   
        qn = Question.objects.all()
        return render(request,'delete.html',{"qn":qn})

def edit(request):
    if request.method == "POST":
        qid=request.POST.get('qid')
        qd=request.POST.get('qn')
        option1=request.POST.get('option1')
        option2=request.POST.get('option2')
        option3=request.POST.get('option3')
        option4=request.POST.get('option4')
        Question.objects.filter(qid=qid).update(qid=qid,question=qd,option1=option1,option2=option2,option3=option3,option4=option4)
    
        # return HttpResponse("updated")
        messages.success(request, 'Successfully updated')
        return redirect("/edit")
    else:   
        qn = Question.objects.all()
        return render(request,'edit.html',{"qn":qn})
    return render(request,'viewqn.html')

def result(request):
    # print('Session email : ',request.session.get('email'))
    s_email=request.session.get('email')
    score=0
    std=Registration.objects.filter(email=s_email)

    try:
        for i in range(0 , len(lst)):
            if lst[i]==anslst[i]:
                score +=1

            
        if request.method=="POST":
            sname=request.POST.get('sname')
            s_email=request.POST['s_email']
            marks=request.POST['marks']
            results=Result(marks=marks,s_email=s_email,sname=sname)
            results.save()
            return redirect('home')
        else:
           return render(request,'result.html',{"score":score,"s_email":s_email,"std":std})
    except IndexError:
        print("IndexError")
        return render(request,'result.html',{"score":score,"s_email":s_email})


def tresult(request):
    result=Result.objects.all()
    return render(request,'tresult.html',{"result":result})
    
def saves(request):
   
    ans = request.GET['ans']
    print(ans)
    lst.append(ans)
    return HttpResponse("sumitted")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

    

# def success(request):
#     user =Registration.objects.get(id=request.session['id'])
#     context = {
#         "user": user
#     }
#     return render(request, 'register/success.html', context)