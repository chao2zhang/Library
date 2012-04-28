# -*- coding: utf-8 -*-
# Create your views here.here.
from django import forms
from models import Sale
from books.models import Book
from members.models import Member
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

class SaleForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label=u'书目')
    member = forms.ModelChoiceField(queryset=Member.objects.all(), label=u'会员')
    count = forms.IntegerField(min_value=0, label=u'数量')
    def clean_count(self):
    class Meta:
        model = Sale
        exclude = ('create_at', 'update_at')

@login_required
def index(request):
    sales = Sale.objects.all()
    return render_to_response('sales/index.html', {'sales': sales}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = SaleForm()
    if request.POST:
        form = SaleForm(request.POST)
        if form.is_valid():
            book = form.book
            if book.count < form.count:
                return redirect('error/not_enough_books.html', {'book':book}, context_instance=RequestContext(request))
            book.count -= form.count
            form.save()
            book.save()
            return redirect(index)
    return render_to_response('sales/new.html', {'form':form}, context_instance=RequestContext(request))
