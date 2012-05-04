# -*- coding: utf-8 -*-
# Create your views here.here.
from django import forms
from models import Sale
from books.models import Book
from members.models import Member
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
import datetime

class SaleForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label=u'书目')
    member = forms.ModelChoiceField(queryset=Member.objects.filter(valid_to__gte=datetime.date.today(), valid=1), required=False, label=u'会员', empty_label=u'匿名')
    password = forms.CharField(max_length=16, label=u'密码', widget=forms.PasswordInput, required=False)
    count = forms.IntegerField(min_value=1, label=u'数量')
    def clean(self):
        cd = self.cleaned_data
        if cd['count'] > cd['book'].count:
            raise ValidationError(u'存货不够，当前存货量为%i。' % cd['book'].count)
        if cd['member']:
            mb = cd['member']
            if not(cd['password'] and mb.check_password(cd['password'])):
                raise ValidationError(u'密码错误')
            dc = 1
            if mb.group:
                dc = mb.group.discount
            cost = cd['count'] * cd['book'].sale_price * dc
            if mb.balance < cost:
                raise ValidationError(u'余额不足，当前余额为%.2f。' % mb.balance)
        return self.cleaned_data
    class Meta:
        model = Sale
        exclude = ('create_at', 'update_at')

@login_required
def index(request):
    sales = Sale.objects.all()
    return render_to_response('sales/index.html', {'sales': sales, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = SaleForm()
    if request.POST:
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            sale.new()
            request.flash['message']=u'添加成功'
            return redirect(index)
    return render_to_response('sales/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def show(request, id):
    id = int(id)
    sale = get_object_or_404(Sale, pk=id)
    return render_to_response('sales/show.html', {'sale':sale, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def delete(request, id):
    id = int(id)
    sale = get_object_or_404(Sale, pk=id)
    sale.delete()
    request.flash['message']=u'删除成功'
    return redirect(index)