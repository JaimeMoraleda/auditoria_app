from flask import Blueprint, render_template, request, redirect
from db import get_conn

asignaturas_bp = Blueprint(
    "asignaturas",
    __name__
)

@asignaturas_bp.route("/asignaturas")
def asignaturas():

    from flask import request

    nombre = request.args.get("nombre","")

    precio = request.args.get("precio","")

    limit = request.args.get("limit",5)

    offset = request.args.get("offset",0)

    conn = get_conn()

    cur = conn.cursor()

    sql = """
        SELECT *
        FROM asignaturas
        WHERE nombre ILIKE %s
    """

    params = [f"%{nombre}%"]

    if precio != "":

        sql += " AND precio <= %s "

        params.append(precio)

    sql += " ORDER BY asignatura_id "

    sql += " LIMIT %s OFFSET %s "

    params.append(limit)

    params.append(offset)

    cur.execute(sql,params)

    asignaturas = cur.fetchall()

    conn.close()

    return render_template(
        "asignaturas.html",
        asignaturas=asignaturas
    )

@asignaturas_bp.route(
    "/asignatura/add",
    methods=["POST"]
)
def add_asignatura():

    nombre = request.form["nombre"]

    precio = request.form["precio"]

    max_alumnos = request.form["max_alumnos"]

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
    """
    INSERT INTO asignaturas(
        nombre,
        precio,
        max_alumnos
    )
    VALUES(%s,%s,%s)
    """,
    (nombre, precio, max_alumnos)
)

    conn.commit()
    conn.close()

    return redirect("/asignaturas")

@asignaturas_bp.route(
    "/asignatura/update/<id>",
    methods=["POST"]
)
def update_asignatura(id):

    nombre = request.form["nombre"]
    
    precio = request.form["precio"]

    max_alumnos = request.form["max_alumnos"]

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
    """
    UPDATE asignaturas
    SET nombre=%s,
        precio=%s,
        max_alumnos=%s
    WHERE asignatura_id=%s
    """,
    (
        nombre,
        precio,
        max_alumnos,
        id
    )
)

    conn.commit()
    conn.close()

    return redirect("/asignaturas")

@asignaturas_bp.route(
    "/asignatura/delete/<id>"
)
def delete_asignatura(id):

    conn = get_conn()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM asignaturas
        WHERE asignatura_id=%s
        """,
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/asignaturas")