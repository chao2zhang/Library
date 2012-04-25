# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import RequestContext
from models import Book


class BookForm(forms.ModelForm):
    isbn = forms.RegexField(regex='^[0-9]{13}', label=u'ISBN编号')
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=200)
    press = forms.CharField(max_length=200)
    class Meta:
        model = Book
        exclude = ('count', 'create_at', 'update_at')

@login_required
def index(request):
    books = Book.objects.all()
    return render_to_response('books/index.html', {'books':books}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = BookForm()
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('books/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):
    book = get_object_or_404(Book, id)
    form = BookForm(book);
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('books/edit.html', {'form':form}, context_instance=RequestContext(request))
    
