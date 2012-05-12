# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from models import Purchase
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404
from histories.models import History

class PurchaseForm(forms.ModelForm):#新进货的表单结构
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label=u'书目')
    price = forms.FloatField(min_value=0, label=u'进货价')
    count = forms.IntegerField(min_value=1, label=u'数量')
    class Meta:
        model = Purchase
        exclude = ('paid', 'create_at', 'update_at')

def add_history(user, content, topup, link):#记录进货相关操作
    if link:
        History(user=user, content=content, klass='Purchase', unicode=topup, url=topup.get_absolute_url()).save()
    else:
        History(user=user, content=content, klass='Purchase', unicode=topup).save()
        
def index(request):#进货列表
    purchases = Purchase.objects.all()
    return render_to_response('purchases/index.html', {'purchases': purchases, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def new(request):#添加进货
    form = PurchaseForm()
    if request.POST:
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            request.flash['message']=u'添加成功'
            add_history(request.user, u'添加进货', purchase, True)
            return redirect(purchase)
    return render_to_response('purchases/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):#编辑指定进货
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    if purchase.paid == 1:
        raise Http404 
    form = PurchaseForm(instance=purchase);
    if request.POST:
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            request.flash['message']=u'保存成功'
            add_history(request.user, u'编辑进货', purchase, True)
            return redirect(purchase)
    return render_to_response('purchases/edit.html', {'form': form, 'id': id}, context_instance=RequestContext(request))

@login_required
def delete(request, id):#删除指定进货
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    purchase.delete()
    request.flash['message']=u'删除成功'
    add_history(request.user, u'删除进货', purchase, False)
    return redirect(index)

@login_required
def show(request, id):#显示指定进货详细信息
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    if purchase.paid == 0:
        paybutton = 1
    return render_to_response('purchases/show.html', {'purchase': purchase, 'message': request.flash.get('message')}, context_instance=RequestContext(request))
    
@login_required
def pay(request, id):#完成指定进货
    id = int(id)
    purchase = get_object_or_404(Purchase, pk=id)
    purchase.pay()
    request.flash['message']=u'支付成功'
    add_history(request.user, u'支付进货', purchase, True)
    return redirect(purchase)
