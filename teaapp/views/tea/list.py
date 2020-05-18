import sqlite3
from django.shortcuts import render, redirect, reverse
from teaapp.models import Tea, Packaging
from ..connection import Connection

def tea_list(request):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT * FROM teaapp_tea
            ORDER BY tea_name
            """)

            all_teas = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                tea = Tea()
                tea.id = row['id']
                tea.name = row['tea_name']
                tea.flavor = row['flavor']

                all_teas.append(tea)

        template = 'tea/list.html'
        context = {
            'all_teas': all_teas
        }

        return render(request, template, context)

    elif request.method == "POST":
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO teaapp_tea
            (tea_name, flavor)
            VALUES (?, ?)
            """,
            (form_data['name'], form_data['flavor']))

            db_cursor.execute("""
            INSERT INTO teaapp_teapackaging
            (
                longevity_in_months, packaging_id, 
                tea_id
            )
            VALUES (?, ?, ?)
            """,
            (form_data['name'], form_data['flavor']))

        return redirect(reverse('teaapp:tea_list'))