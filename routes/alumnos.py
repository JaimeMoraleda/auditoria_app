from flask import Blueprint, render_template, request, redirect
from db import get_conn

alumnos_bp = Blueprint(
    "alumnos",
    __name__
)

@alumnos_bp.route(
    "/alumno/add",
    methods=["POST"]
)
@alumnos_bp.route("/alumnos")
def alumnos():

    from flask import request

    nombre = request.args.get("nombre","")

    dinero = request.args.get("dinero","")

    limit = request.args.get("limit",5)

    offset = request.args.get("offset",0)

    conn = get_conn()

    cur = conn.cursor()

    sql = """
        SELECT *
        FROM alumnos
        WHERE nombre ILIKE %s
    """

    params = [f"%{nombre}%"]

    if dinero != "":

        sql += " AND dinero >= %s "

        params.append(dinero)

    sql += " ORDER BY alumno_id "

    sql += " LIMIT %s OFFSET %s "

    params.append(limit)

    params.append(offset)

    cur.execute(sql,params)

    alumnos = cur.fetchall()

    conn.close()

    return render_template(
        "alumnos.html",
        alumnos=alumnos
    )

@alumnos_bp.route(
    "/alumno/update/<id>",
    methods=["POST"]
)
def update_alumno(id):

    nombre = request.form["nombre"]

    email = request.form["email"]

    dinero = request.form["dinero"]

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
    """
    UPDATE alumnos
    SET nombre=%s,
        email=%s,
        dinero=%s
    WHERE alumno_id=%s
    """,
    (nombre, email, dinero, id)
)

    conn.commit()
    conn.close()

    return redirect("/alumnos")

@alumnos_bp.route(
    "/alumno/delete/<id>"
)
def delete_alumno(id):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM alumnos
        WHERE alumno_id=%s
        """,
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/alumnos")