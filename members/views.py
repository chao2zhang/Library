# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Member
from groups.models import Group

class GroupForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label=u'姓名')
    password = forms.CharField(max_length=128, label=u'密码', widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=Member.GENDER_CHOICES, label=u'性别')
    birthday = forms.DateField(widget=forms.DateInput, label=u'生日')
    valid_to = forms.DateField(widget=forms.DateInput, label=u'有效期至')
    valid = forms.BooleanField(required=False, widget=forms.CheckboxInput, label=u'是否有效')
    identify_number = forms.RegexField(regex='^[0-9]{18}$', label=u'身份证')
    group = forms.ModelChoiceField(required=False, queryset=Group.objects.all(), label=u'会员组')
    class Meta:
        model = Member
        exclude = ('balance', 'point', 'create_at', 'update_at')

def index(request):
    members = Member.objects.all()
    return render_to_response('members/index.html', {'members':members}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = GroupForm()
    if request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
    return render_to_response('members/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):
    id = int(id)
    member = get_object_or_404(Member, pk=id)
    form = GroupForm(instance=member);
    if request.POST:
        form = GroupForm(request.POST, instance=member)
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


