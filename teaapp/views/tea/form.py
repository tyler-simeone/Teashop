import sqlite3
from django.shortcuts import render
from ..connection import Connection
from .details import get_tea

def tea_form(request):
    if request.method == "GET":
        template = 'tea/form.html'
        context = {}

        return render(request, template, context)

def tea_edit_form(request, tea_id):
    if request.method == 'GET':
        tea = get_tea(tea_id)

        template = 'tea/form.html'
        context = {
            'tea': tea
        }

        return render(request, template, context)