from django.shortcuts import render,redirect
from .forms import BusinessForm,ChatForm,ProfileUpdateForm,ProfileForm
from django.contrib import messages
from .models import Business,Chat,Profile,Neighborhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def  index(request):
    chats=Chat.objects.all()
    return render(request,'main/index.html',{"chats":chats})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def businesses(request):
    business=Business.objects.all()
    return render(request,'main/businesses.html',{"business":business})

@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def profile(request,id):
    profile_data = User.objects.get(id=id)
    current_user = request.user
    if request.method =='POST':
        profile=ProfileUpdateForm(request.POST,request.FILES,instance=current_user.profile)
        if profile.is_valid():
            message.success(request,'Your profile has been updated!')
            return redirect('profile')
    else:
        profile=ProfileUpdateForm(instance=request.user)
    context={"profile":profile,"current_user": current_user,"profile_data":profile_data}
    return render(request, 'main/profile.html',context)

@login_required(login_url='/accounts/login/')
def updateprofile(request):
    current_user = request.user
    profile=Profile.objects.all()
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES) 

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'main/updateprofile.html',{"form": form} )

@login_required(login_url='/accounts/login/')
def single_business(request,id):
    try:
        business=Business.objects.get(id=id)
    except DoesNotExist:
        raise Http404()
    return render(request,'main/single_business.html',{'business':business})

def neighbor(request):
    neighbor=Neighborhood.objects.all()
    return render(request,'main/places.html',{'neighbor':neighbor})

@login_required(login_url='/accounts/login/')
def search(request):
    if 'Search' in request.GET and request.GET['Search']:
        search_term=request.GET.get('Search')
        searched_results=Business.search(search_term)
        message=f"{search_term}"
        
        return render(request,'main/search.html',{"message":message,"results":searched_results})
    else:
        message="You haven't searched for any term"
        return render(request,"main/search.html",{"message":message})

