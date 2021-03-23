from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from blog.models import Posts
from django.contrib.auth.models import User
from .decorator import unauthenticated_user,authenticated_user
import re


# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
@authenticated_user
def contact(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone=request.POST['phone']
        email=request.POST['email']
        msg=request.POST['msg']
        if len(fname)<3 or len(lname)<3 or len(email)<5 or len(phone)<10 or len(msg)<5:
            messages.error(request,'Please fill the form correctly')
        else:
            contact=Contact(fname=fname,lname=lname,phone=phone,email=email,content=msg)
            contact.save()
            messages.success(request,'Your form submitted successfully')
    return render(request,'home/contact.html')

def search(request):
    query=request.GET['search']
    if(len(query)>70):
        cover=Posts.objects.none()
    else:
        allpoststitle=Posts.objects.filter(title__icontains=query)
        allpostscontent=Posts.objects.filter(content__icontains=query)
        allpostsauthor=Posts.objects.filter(author__icontains=query)
        cover=allpoststitle.union(allpostscontent,allpostsauthor)
    
    if cover.count()==0:  
         messages.warning(request,'Search result is not found')  
    context={'allsearch':cover,'query':query}
    return render(request,'home/search.html',context)
@unauthenticated_user
def signUp(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        password = "R@m@_f0rtu9e$"
    #check for the error
        if len(username) < 5:
            messages.error(request,'Username length must be greater than 4')
            return redirect('signUp')
        if not username.isalnum():
            messages.error(request,'Username must contain only alphabet or number')
            return redirect('signUp')
        if not fname.isalpha() or not lname.isalpha() or len(fname) < 3 or len(lname) < 3:
            messages.error(request,'first name and last name must contain only alphabet')
            return redirect('signUp')
        if not re.search(regex,email):
            messages.error(request,'email should be in formte example213@gmail.com')
            return redirect('signUp')
        if pass1!=pass2:
            messages.error(request,'Password did not match')
            return redirect('signUp')
        elif (len(pass1)<8): 
            messages.error('password must contain number,alphabet,specialcharacter,atleast 1 capital alphabet and length greater than 7')
            return redirect('signUp')
        elif not re.search("[a-z]", pass1): 
            messages.error('password must contain number,alphabet,specialcharacter,atleast 1 capital alphabet and length greater than 7')
            return redirect('signUp')
        elif not re.search("[A-Z]", password): 
            messages.error('password must contain number,alphabet,specialcharacter,atleast 1 capital alphabet and length greater than 7')
            return redirect('signUp')        
        elif not re.search("[0-9]", password):
            messages.error('password must contain number,alphabet,specialcharacter,atleast 1 capital alphabet and length greater than 7') 
            return redirect('signUp')
        elif not re.search("[_@$]", password):
            messages.error('password must contain number,alphabet,specialcharacter,atleast 1 capital alphabet and length greater than 7') 
            return redirect('signUp')
        elif re.search("\s", password):
            messages.error('password must contain number,alphabet,specialcharacter,atleast 1 capital alphabet and length greater than 7') 
            return redirect('signUp')

    #create the user
        user=User.objects.create_user(username=username,email=email,password=pass1)  
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request,"You have successfully created your account") 
        return redirect('signUp')
    else:
        return render(request,'home/signUp.html')     
@unauthenticated_user    
def signIn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,'You are succesfully login')
            return redirect('home')
        else:
            messages.error(request,'credentials are invalid')
            return redirect('signIn')     
    return render(request,'home/signIn.html')
@authenticated_user
def signOut(request):
    logout(request)
    messages.success(request,'You are succesfully logout')
    print("helo")
    return redirect('home')
def profile(request):
    user=User.objects.all()
    print(user.first_name)
    print("hello")
    return render(request,'home/profile.html')