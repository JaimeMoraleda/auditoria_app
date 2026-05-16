from flask import Blueprint, render_template, request, redirect
from db import get_conn

profesores_bp = Blueprint(
    "profesores",
    __name__
)

@profesores_bp.route("/profesores")
def profesores():

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM profesores"
    )

    profesores = cur.fetchall()

    conn.close()

    return render_template(
        "profesores.html",
        profesores=profesores
    )

@profesores_bp.route(
    "/profesor/add",
    methods=["POST"]
)
def add_profesor():

    nombre = request.form["nombre"]

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO profesores(nombre)
        VALUES(%s)
        """,
        (nombre,)
    )

    conn.commit()
    conn.close()

    return redirect("/profesores")

@profesores_bp.route(
    "/profesor/update/<id>",
    methods=["POST"]
)
def update_profesor(id):

    nombre = request.form["nombre"]

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE profesores
        SET nombre=%s
        WHERE profesor_id=%s
        """,
        (nombre, id)
    )

    conn.commit()
    conn.close()

    return redirect("/profesores")

@profesores_bp.route(
    "/profesor/delete/<id>"
)
def delete_profesor(id):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM profesores
        WHERE profesor_id=%s
        """,
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/profesores")