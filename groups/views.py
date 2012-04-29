# -*- coding: utf-8 -*-
# Create your views here.
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from models import Group

class MemberForm(forms.ModelForm):
    name = forms.CharField(max_length=200, label=u'名称')
    discount = forms.FloatField(label=u'折扣')
    class Meta:
        model = Group
        exclude = ('create_at', 'update_at')

def index(request):
    groups = Group.objects.all()
    return render_to_response('groups/index.html', {'groups':groups}, context_instance=RequestContext(request))

@login_required
def new(request):
    form = MemberForm()
    if request.POST:
        form = MemberForm(request.POST)
        if form.is_valid():
            group = form.save()
            return redirect(group)
    return render_to_response('groups/new.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def edit(request, id):
    id = int(id)
    group = get_object_or_404(Group, pk=id)
    form = MemberForm(instance=group);
    if request.POST:
        form = MemberForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect(group)
    return render_to_response('groups/edit.html', {'form': form, 'id': id}, context_instance=RequestContext(request))

@login_required
def delete(request, id):
    id = int(id)
    group = get_object_or_404(Group, pk=id)
    group.delete()
    return redirect(index)

@login_required
def show(request, id):
    id = int(id)
    group = get_object_or_404(Group, pk=id)
    return render_to_response('groups/show.html', {'group': group}, context_instance=RequestContext(request))


