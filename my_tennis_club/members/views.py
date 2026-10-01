from django.http import HttpResponse
from django.template import loader

from .models import Member

def members(request):
    all_members = Member.objects.all()
    template = loader.get_template('all_members.html')
    context = {
        'members': all_members,
    }
    return HttpResponse(template.render(context, request))