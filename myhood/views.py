from django.shortcuts import render
from .forms import BusinessForm

def  index(request):
    
    return render(request,'main/index.html')

def  add_post(request):
    form= BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            message.success(request,"Post sent successfully!")
            return redirect('index')
        else:
            form = BusinessForm()
    context={
        "form": form,
    }
    return render(request,'main/add_post.html',context)