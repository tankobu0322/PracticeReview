from django.shortcuts import render,redirect
from .models import Chorus
from .forms import ChoursForm

def index(request):
    return render(request,"review/index.html")

def upload_chorus(request):
    if request.method == 'POST':
        form = ChoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ChoursForm()
        return render(request, "review/upload.html",{'form': form})
    
def upload_success(request):
    return render(request, "review/upload_success.html")

def watch_review(request):
    chorus = Chorus.objects.all()
    return render(request,"review/watchReview.html",{"chorus":chorus})