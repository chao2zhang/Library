# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from models import Purchase
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext


class PurchaseForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label=u'书目')
    price = forms.FloatField(min_value=0, label=u'进货价')
    count = forms.IntegerField(min_value=0, label=u'数量')
    class Meta:
        model = Purchase
        exclude = ('paid', 'create_at', 'update_at')


def index(request):
    purchases = Purchase.objects.all()
    return render_to_response('purchases/index.html', {'purchases': purchases}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = PurchaseForm()
    if request.POST:
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('purchases/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    form = PurchaseForm(instance=purchase);
    if request.POST:
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('purchases/edit.html', {'form': form, 'id': id}, context_instance=RequestContext(request))

@login_required
def delete(request, id):
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    purchase.delete()
    return redirect(index)

@login_required
def show(request, id):
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    if purchase.paid == 0:
        paybutton = 1
    return render_to_response('purchases/show.html', {'purchase': purchase}, context_instance=RequestContext(request))
    
@login_required
def setPaid(request, id):
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    purchase.paid = 1
    purchase.save()
    book = Book.objects.get(id = purchase.book_id)
    book.count += purchase.count
    book.save()
    return render_to_response('purchases/show.html', {'purchase': purchase}, context_instance=RequestContext(request))

