from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import householdAccount
from .forms import householdAccountForm
# Create your views here.

def index(request):
    listOfHouseholdAccount=householdAccount.objects.all().order_by('id')
    return render(request,"crud/index.html",{'householdAccounts':listOfHouseholdAccount})
def show(request,id=None):
    rec= get_object_or_404(householdAccount,pk=id)
    return render(request,"crud/show.html",{'rec':rec})

def edit(request,id=None):
    target_note= get_object_or_404(householdAccount,pk=id)
    if request.method=="POST":
        form = householdAccountForm(request.POST,instance=target_note)
        if form.is_valid():
            target_note=form.save(commit=False)
            target_note.save()
            return redirect('crud:index')
    else:
        form = householdAccountForm(instance=target_note)
        return render(request, 'crud/edit.html',dict(form=form,id=id))

def create(request):
    note= householdAccount()
    if request.method=="POST":
        form = householdAccountForm(request.POST,instance=note)
        if form.is_valid():
            note=form.save(commit=False)
            note.save()
            return redirect('crud:index')
    else:
        form = householdAccountForm(instance=note)
    return render(request,'crud/create.html',{'form':form})

def delete(request,id=None):
    target=get_object_or_404(householdAccount,pk=id)
    target.delete()
    return redirect('crud:index')
