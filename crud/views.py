from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import householdAccount
from .forms import householdAccountForm
from django.contrib.auth.models import User
import io
import csv
import urllib
# Create your views here.
@login_required
def index(request):
    user_id=request.user.id
    listOfHouseholdAccount=householdAccount.objects.filter(user=user_id).all
    #listOfHouseholdAccount=householdAccount.objects.all().order_by('id')
    return render(request,"crud/index.html",{'householdAccounts':listOfHouseholdAccount})

@login_required
def show(request,id=None):
    rec= get_object_or_404(householdAccount.objects.filter(user=request.user.id),pk=id)
    return render(request,"crud/show.html",{'rec':rec})

@login_required
def edit(request,id=None):
    target_note= get_object_or_404(householdAccount.objects.filter(user=request.user.id),pk=id)
    if request.method=="POST":
        form = householdAccountForm(request.POST,instance=target_note)
        if form.is_valid():
            target_note=form.save(commit=False)
            target_note.save()
            return redirect('crud:index')
    else:
        form = householdAccountForm(instance=target_note)
        return render(request, 'crud/edit.html',dict(form=form,id=id))

@login_required
def create(request):
    note= householdAccount()
    if request.method=="POST":
        form = householdAccountForm(request.POST,instance=note)
        if form.is_valid():
            note=form.save(commit=False)
            note.user=request.user
            note.save()
            return redirect('crud:index')
    else:
        form = householdAccountForm(instance=note)
    return render(request,'crud/create.html',{'form':form})

@login_required
def delete(request,id=None):
    if request.method=="POST":
        target=get_object_or_404(householdAccount.objects.filter(user=request.user.id),pk=id)
        target.delete()
        return redirect('crud:index')
    else:
        return redirect('crud:index')

@login_required
def download(request,id=None):
    response=HttpResponse(content_type='text/csv; charset=utf-8')
    filename = urllib.parse.quote((u'ItemData.csv').encode("utf-8"))
    response['Content-Disposition']='attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer=csv.writer(response)
    writer.writerow(['Item','Price','category','Memo','Created_at'])
    note=get_object_or_404(householdAccount.objects.filter(user=request.user.id), pk=id)
    writer.writerow([note.item,note.price,note.category,note.memo,note.created_at])
    return response


@login_required
def download_all(request):
    response=HttpResponse(content_type='text/csv; charset=utf-8')
    filename = urllib.parse.quote((u'allData.csv').encode("utf-8"))
    response['Content-Disposition']='attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer=csv.writer(response)
    writer.writerow(['Item','Price','category','Memo','Created_at'])
    for note in householdAccount.objects.filter(user=request.user.id).all():
        writer.writerow([note.item,note.price,note.category,note.memo,note.created_at])
    return response

