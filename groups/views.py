# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Group
from histories.models import History

class MemberForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label=u'名称')
    discount = forms.FloatField(min_value=0.0, max_value=1.0, label=u'折扣')
    class Meta:
        model = Group
        exclude = ('create_at', 'update_at')

def add_history(user, content, topup, link):
    if link:
        History(user=user, content=content, klass='Group', unicode=topup, url=topup.get_absolute_url()).save()
    else:
        History(user=user, content=content, klass='Group', unicode=topup).save()

def index(request):#显示会员组列表
    groups = Group.objects.all()
    return render_to_response('groups/index.html', {'groups':groups, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def new(request):#新增会员组
    form = MemberForm()
    if request.POST:
        form = MemberForm(request.POST)
        if form.is_valid():
            group = form.save()
            request.flash['message']=u'添加成功'
            add_history(request.user, u'添加会员组', group, True)
            return redirect(group)
    return render_to_response('groups/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):#编辑指定会员组
    id = int(id)
    group = get_object_or_404(Group, pk=id)
    form = MemberForm(instance=group);
    if request.POST:
        form = MemberForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            request.flash['message']=u'保存成功'
            add_history(request.user, u'编辑会员组', group, True)
            return redirect(group)
    return render_to_response('groups/edit.html', {'form': form, 'id': id}, context_instance=RequestContext(request))

@login_required
def delete(request, id):#删除指定会员组
    id = int(id)
    group = get_object_or_404(Group, pk=id)
    add_history(request.user, u'删除会员组', group, False)
    group.delete()
    request.flash['message']=u'删除成功'
    return redirect(index)

@login_required
def show(request, id):#显示指定会员组详细信息
    id = int(id)
    group = get_object_or_404(Group, pk=id)
    return render_to_response('groups/show.html', {'group': group, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

