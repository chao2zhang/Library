# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def home(request):
    return render_to_response('manage/home.html', context_instance=RequestContext(request))
