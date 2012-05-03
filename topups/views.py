# -*- coding: utf-8 -*-
# Create your views here.
from models import Topup
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

def index(request):
    topups = Topup.objects.all()
    return render_to_response('topups/index.html', {'topups': topups, 'message': request.flash.get('message')}, context_instance=RequestContext(request))

@login_required
def delete(request, id):
    id = int(id)
    topup = get_object_or_404(Topup, pk=id)
    topup.delete()
    request.flash['message']=u'删除成功'
    return redirect(index)
