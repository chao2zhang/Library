# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Member
from groups.models import Group

class MemberForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label=u'姓名')
    password = forms.CharField(max_length=16, label=u'密码', widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=Member.GENDER_CHOICES, label=u'性别')
    birthday = forms.DateField(widget=forms.DateInput, label=u'生日')
    valid_to = forms.DateField(widget=forms.DateInput, label=u'有效期至')
    valid = forms.BooleanField(required=False, widget=forms.CheckboxInput, label=u'是否有效')
    identify_number = forms.RegexField(regex='^[0-9]{18}$', label=u'身份证')
    group = forms.ModelChoiceField(required=False, queryset=Group.objects.all(), label=u'会员组')
    def clean_password(self):
        d = self.cleaned_data
        m = self.instance
        if not m.check_password(d['password']):
            raise ValidationError(u'密码不正确')
        return d['password']
    class Meta:
        model = Member
        exclude = ('password', 'balance', 'point', 'create_at', 'update_at')
        
class MemberChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=16, label=u'原密码', widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=16, label=u'新密码', widget=forms.PasswordInput)
    new_password_confirm = forms.CharField(max_length=16, label=u'新密码确认', widget=forms.PasswordInput)
    def __init__(self, instance, *args, **kwargs):
        self.instance = instance
        super(MemberChangePasswordForm, self).__init__(*args, **kwargs)
    def clean(self):
        d = self.cleaned_data
        m = self.instance
        if not m.check_password(d['password']):
            raise ValidationError(u'密码不正确')
        if (cmp(d['new_password'], d['new_password_confirm']) != 0):
            raise ValidationError(u'两次密码不一致')
        return d
    def save(self):        
        d = self.cleaned_data
        m = self.instance
        m.set_password(d['new_password'])
        m.save()
        return m
    

def index(request):
    members = Member.objects.all()
    return render_to_response('members/index.html', {'members':members}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = MemberForm()
    if request.POST:
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('members/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):
    id = int(id)
    member = get_object_or_404(Member, pk=id)
    form = MemberForm(instance=member);
    if request.POST:
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('members/edit.html', {'form': form, 'id': id}, context_instance=RequestContext(request))

@login_required
def delete(request, id):
    id = int(id)
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect(index)

@login_required
def show(request, id):
    id = int(id)
    member = get_object_or_404(Member, pk=id)
    return render_to_response('members/show.html', {'member': member}, context_instance=RequestContext(request))

@login_required
def change_password(request, id):
    id = int(id)
    member = get_object_or_404(Member, pk=id)
    form = MemberChangePasswordForm(member)
    if request.POST:
        form = MemberChangePasswordForm(member, request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('members/change_password.html', {'form': form}, context_instance=RequestContext(request))
