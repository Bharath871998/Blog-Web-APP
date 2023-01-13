from django.shortcuts import render , redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Post
from .forms import BlogForm
# Create your views here.


def home(request):
    posts = Post.objects.filter(status="published")
    return render(request,'home.html',{'posts':posts})
    
    # return render(request, "home.html")


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
    else:
        return render(request,'signup.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, "login.html")


def detail_post(request, id):
    readmore = Post.objects.filter(status = "published", id=id)
    return render(request, 'detailpost.html', {'posts': readmore})


def logout(request):
    auth.logout(request)    
    return redirect("/")


def mypost(request):
    posts = Post.objects.all()
    return render(request,'mypost.html',{'posts':posts})


def createpost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BlogForm()   
    return render(request, 'createpost.html',{'form': form})


def edit(request, id = 0):
    if request.method == 'GET':
        if id == 0:
            form = BlogForm()
        else:
            blog = Post.objects.get(id = id)
            bform = BlogForm(instance=blog)
        return render(request, 'editpost.html', {'form': bform})
    else:
        if id == 0:
            bform = BlogForm(request.POST)
        else:
            form = Post.objects.get(id=id)
            bf = BlogForm(request.POST, instance = form)
            if bf.is_valid():
                bf.save()
                return redirect('/')
            else:
                return render(request, 'editpost.html', {'form': bform})
            
            
def delete(request,id):
    dform = Post.objects.get(id=id)
    dform.delete()
    return redirect('/')