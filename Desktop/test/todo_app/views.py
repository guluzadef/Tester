from django.shortcuts import render, redirect
from .forms import Add
from .models import *
import facebook
import json
# Create your views here.
from rest_framework import permissions
from rest_framework import viewsets


def test(request):
    context = {}
    context['form'] = Add()

    if request.method == 'POST':
        form = Add(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'index.html', context)


def files(request):
    file = FB.objects.filter(id=1).last()
    token = 'EAAC7ehlAHnQBAG4NqtfNKeMJi3oz1IPsrauMjnLIgvQy7oIkDFV5xJ8AHfNC3DZBwjy0zG2QYsKOBtOUu6WXDBZCqvt3wePzVSqRwdr2BZCaMIN7S4Cwe3rddsl2ih0LQdQLik1mZAIP3QJVVpJLutiiQWUymb5m7F4qTKqQtAZDZD'
    fb = facebook.GraphAPI(access_token=token)
    share = fb.put_object(parent_object=file, connection_name='me')
    # print(share)
    return render(request, 'fb.html')
