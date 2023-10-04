
from django.contrib.auth.decorators import login_required
from .models import blog
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission, User
from django.contrib.contenttypes.models import ContentType


# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def SignupPage(request):
    if request.method=="POST":
        email=request.POST.get("email")
        username=request.POST.get('username')
        password=request.POST.get('password')
        repass=request.POST.get('repass')

        if repass==password:
            my_user=User.objects.create_user(email,username,password)
            my_user.save()
            return redirect("login")

        else:
            return HttpResponse("Incorrect Username/Password")

    return render(request,'signup.html')


def LoginPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)
        user = User.objects.filter(email=email).first()

        if user is not None:
            auth_user = authenticate(request, username=user.username, password=password)

            if auth_user is not None:
                login(request, auth_user)
                return redirect('home')

            else:
                return HttpResponse("Incorrect password!!")

        else:
            return HttpResponse("User not found!!")

    return render(request, 'login.html')



@login_required(login_url='login')
def  CreatePage(request):
    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        usr=blog.objects.create(title=title, content=content, author=author)
        usr.save()
    return render(request,'create.html')

def Logout(request):
    logout(request)
    return redirect('login')


def ViewPage(request):
    blogs=blog.objects.all()
    context={
        'blogs':blogs,
    }
    return render(request,'view.html',context)

def Remove(request,id):
    a=blog.objects.get(id=id)
    a.delete()
    return redirect("view")


def Update(request,id):
    bg=blog.objects.get(id=id)
    return render(request,'update.html',{'bg':bg})


def Uprec(request, id):
    title=request.POST['title']
    content=request.POST['content']
    author=request.POST['author']
    blog_reg=blog.objects.get(id=id)
    blog_reg.title=title
    blog_reg.content=content
    blog_reg.author=author
    blog_reg.save()
    return redirect("view")
