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

def details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Banana', 'Orange']
    }
    return HttpResponse(template.render(context, request))