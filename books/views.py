# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Book
from helper import helper
from histories.models import History

class BookForm(forms.ModelForm):#用于生成一条Book记录的表单结构
    isbn = forms.RegexField(regex='^[0-9]{13}$', label=u'ISBN编号')
    title = forms.CharField(max_length=200, label=u'标题')
    author = forms.CharField(max_length=200, label=u'作者')
    press = forms.CharField(max_length=200, label=u'出版社')
    sale_price = forms.FloatField(min_value=0.01, label=u'零售价')
    class Meta:
        model = Book
        exclude = ('count', 'create_at', 'update_at')

class BookSearchForm(forms.Form):#用于搜索数目信息的表单结构
    id = forms.RegexField(required=False, regex='^[0-9]*$', label=u'编号')
    isbn = forms.CharField(required=False, max_length=13, label=u'ISBN编号')
    title = forms.CharField(required=False, max_length=200, label=u'标题')
    author = forms.CharField(required=False, max_length=200, label=u'作者')
    press = forms.CharField(required=False, max_length=200, label=u'出版社')

def add_history(user, content, topup, link):#记录操作所用的函数
    if link:
        History(user=user, content=content, klass='Book', unicode=topup, url=topup.get_absolute_url()).save()
    else:
        History(user=user, content=content, klass='Book', unicode=topup).save()

def index(request):#显示Book列表
    books = Book.objects.all()
    return render_to_response('books/index.html', {
        'books':books, 
        'message': request.flash.get('message'),
        }, context_instance=RequestContext(request))

@login_required
def new(request):#添加新书目
    form = BookForm()
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            request.flash['message']=u'添加成功'
            add_history(request.user, u'添加书目', book, True)
            return redirect(book)
    return render_to_response('books/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):#编辑指定编号的书目
    id = int(id)
    book = get_object_or_404(Book, pk=id)
    form = BookForm(instance=book);
    if request.POST:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            request.flash['message']=u'保存成功'
            add_history(request.user, u'编辑书目', book, True)
            return redirect(book)
    return render_to_response('books/edit.html', {'form': form, 'id': id}, context_instance=RequestContext(request))

@login_required
def delete(request, id):#删除指定编号的书目
    id = int(id)
    book = get_object_or_404(Book, pk=id)
    add_history(request.user, u'删除书目', book, False)
    book.delete()
    request.flash['message']=u'删除成功'
    return redirect(index)

@login_required
def show(request, id):#显示指定编号书目的详细信息
    id = int(id)
    book = get_object_or_404(Book, pk=id)
    return render_to_response('books/show.html', {'book': book, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def search(request):#搜索数目
    form = BookSearchForm()
    if request.POST:
        form = BookSearchForm(request.POST)
        if form.is_valid():
            d = {}
            for k, v in form.cleaned_data.iteritems():
                if v:
                    d[k] = v
            d['message'] = helper.get_search_message(form.fields, d)
            return redirect(helper.url_with_querystring(reverse(result), d))
    return render_to_response('books/search.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def result(request):#执行搜索书目的请求
    params = ''
    fields = BookSearchForm().fields
    for k in request.GET:
        if k in fields:
            params += '%s__contains="%s",' % (k, request.GET[k])
    query = 'Book.objects.filter(' + params +')'
    books = eval(query)
    return render_to_response('books/result.html', {'books':books, 'message':request.GET.get('message')}, context_instance=RequestContext(request))

