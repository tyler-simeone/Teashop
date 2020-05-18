import sqlite3
from django.shortcuts import render
from ..connection import Connection
from teaapp.models import Packaging
from .details import create_tea

def get_packaging_methods():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_packaging_methods
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            p.id,
            p.name
        FROM teaapp_packaging p
        """)

        return db_cursor.fetchall()

def create_packaging_methods(cursor, row):
    _row = sqlite3.Row(cursor, row)

    packaging = Packaging()
    packaging.id = _row['id']
    packaging.name = _row['name']

    return packaging

def get_one_tea(tea_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_tea
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.tea_name,
            t.flavor,
            p.name packaging_method,
            tp.longevity_in_months,
            tp.packaging_id
        FROM teaapp_tea t
        JOIN teaapp_packaging p
        ON p.id = tp.packaging_id
        JOIN teaapp_teapackaging tp
        ON t.id = tp.tea_id
        WHERE t.id = ?
        """, (tea_id,))

        return db_cursor.fetchone()

def tea_form(request):
    if request.method == "GET":
        methods = get_packaging_methods()
        template = 'tea/form.html'
        context = {
            'all_methods': methods
        }

        return render(request, template, context)

def tea_edit_form(request, tea_id):
    if request.method == 'GET':
        tea = get_one_tea(tea_id)

        template = 'tea/form.html'
        context = {
            'tea': tea
        }

        return render(request, template, context)