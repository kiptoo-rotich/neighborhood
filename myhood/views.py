from django.shortcuts import render,redirect
from .forms import BusinessForm,ChatForm
from django.contrib import messages
from .models import Business,Chat

def  index(request):
    chats=Chat.objects.all()
    return render(request,'main/index.html',{"chats":chats})

def  add_post(request):
    form= BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.user=request.user
            new_post.save()
            return redirect('businesses')
        else:
            form = BusinessForm()
    context={
        "form": form,
    }
    return render(request,'main/add_post.html',context)

def businesses(request):
    business=Business.objects.all()
    return render(request,'main/businesses.html',{"business":business})

def post_chat(request):
    form=ChatForm()
    user=request.user
    if request.method =='POST':
        form=ChatForm(request.POST,request.FILES)
        if form.is_valid():
            new_chat=form.save(commit=False)
            new_chat.user=request.user
            new_chat.save()
            return redirect('index')
        else:
            form=ChatForm()
    context={
        "form": form,
    }
    return render(request,'main/chats.html',context)
