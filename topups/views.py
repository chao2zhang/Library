# -*- coding: utf-8 -*-
# Create your views here.
from models import Topup
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from members.models import Member
from histories.models import History

class TopupForm(forms.Form):#新充值记录的表单结构
    member = forms.ModelChoiceField(queryset=Member.objects.all(), label=u'会员组')
    password = forms.CharField(max_length=16, label=u'密码', widget=forms.PasswordInput)
    amount = forms.FloatField(min_value=0, label=u'金额')
    def __init__(self, instance, *args, **kwargs):
        self.instance = instance
        super(TopupForm, self).__init__(*args, **kwargs)
    def clean(self):
        d = self.cleaned_data
        p = d['password']
        m = d['member']
        if not m.check_password(p):
            raise ValidationError(u'密码不正确')
        return self.cleaned_data
    def save(self):        
        d = self.cleaned_data
        m = d['member']
        m.topup(d['amount'])
        m.save()
        return self

def add_history(user, content, topup, link):#记录充值相关操作
    if link:
        History(user=user, content=content, klass='Topup', unicode=topup, url=topup.get_absolute_url()).save()
    else:
        History(user=user, content=content, klass='Topup', unicode=topup).save()

def index(request):#充值记录列表
    topups = Topup.objects.all()
    return render_to_response('topups/index.html', {'topups': topups, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def new(request):#添加新充值记录
    form = TopupForm()
    if request.POST:
        form = TopupForm(request.POST)
        if form.is_valid():
            topup = form.save()
            request.flash['message']=u'添加成功'
            add_history(request.user, u'添加充值记录', topup, True)
            return redirect(topup)
    return render_to_response('topups/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def delete(request, id):#删除指定充值记录
    id = int(id)
    topup = get_object_or_404(Topup, pk=id)
    topup.delete()
    request.flash['message']=u'删除成功'
    add_history(request.user, u'删除充值记录', topup, False)
    return redirect(index)

@login_required
def show(request, id):#显示指定充值记录详细信息
    id = int(id)
    topup = get_object_or_404(Topup, pk=id)    
    return render_to_response('topups/show.html', {'topup': topup, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

