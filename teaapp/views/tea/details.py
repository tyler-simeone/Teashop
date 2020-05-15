import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from teaapp.models import Tea, TeaPackaging, Packaging
from ..connection import Connection

def get_tea(tea_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_tea
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.name tea_name,
            t.flavor,
            p.name packaging_method,
            tp.longevity_in_months
        FROM teaapp_tea t
        JOIN teaapp_packaging p
        ON p.id = tp.packaging_id
        JOIN teaapp_teapackaging tp
        ON t.id = tp.tea_id
        WHERE t.id = ?
        """, (tea_id,))

        # return db_cursor.fetchone()

        # tea_packagings = db_cursor.fetchall()
        # tea = Tea()
        # tea.package_methods = []

        all_teas = db_cursor.fetchall()
        
        for row in dataset:


def create_tea(cursor, row):
    _row = sqlite3.Row(cursor, row)

    tea = Tea()
    tea.id = _row['id']
    tea.name = _row['tea_name']
    tea.flavor = _row['flavor']
    # tea.packaging_name = _row['packaging_method']
    tea.packaging_longevity = _row['longevity_in_months']
    
    tea.packages = []

    packaging = Packaging()
    packaging.name = _row['packaging_method']

    # tea_packaging = TeaPackaging()
    # tea_packaging.longevity = _row['longevity_in_months']

    # , tea_packaging
    return(tea, packaging)

def tea_details(request, tea_id):
    if request.method == 'GET':
        tea = get_tea(tea_id)

        template = 'tea/details.html'
        context = {
            'tea': tea
        }
    
    return render(request, template, context)