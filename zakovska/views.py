from django.shortcuts import render
from .models import Mark


def mark_list(request):
    marks = Mark.objects.order_by('-date')
    return render(request, '../templates/zakovska.html', {'marks' : marks})

