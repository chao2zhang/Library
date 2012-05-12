# -*- coding: utf-8 -*-
# Create your views here.
from models import History
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

def index(request):#显示操作记录列表
    histories = History.objects.all()
    return render_to_response('histories/index.html', {'histories': histories, 'message': request.flash.get('message')}, context_instance=RequestContext(request))
