# -*- coding: utf-8 -*-
# Create your views here.
from models import Topup
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from members.models import Member

class TopupForm(forms.Form):
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

def index(request):
    topups = Topup.objects.all()
    return render_to_response('topups/index.html', {'topups': topups, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = TopupForm()
    if request.POST:
        form = TopupForm(request.POST)
        if form.is_valid():
            member = form.save()
            request.flash['message']=u'添加成功'
            return redirect(member)
    return render_to_response('topups/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def delete(request, id):
    id = int(id)
    topup = get_object_or_404(Topup, pk=id)
    topup.delete()
    request.flash['message']=u'删除成功'
    return redirect(index)

@login_required
def show(request, id):
    id = int(id)
    topup = get_object_or_404(Topup, pk=id)    
    return render_to_response('topups/show.html', {'topup': topup, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

