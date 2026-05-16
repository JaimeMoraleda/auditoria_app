from flask import Blueprint, render_template, request, redirect
from db import get_conn

matriculas_bp = Blueprint(
    "matriculas",
    __name__
)

@matriculas_bp.route("/matriculas")
def matriculas():

    from flask import request

    fecha = request.args.get("fecha","")

    limit = request.args.get("limit",5)

    offset = request.args.get("offset",0)

    conn = get_conn()

    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM alumnos"
    )

    alumnos = cur.fetchall()

    cur.execute(
        "SELECT * FROM asignaturas"
    )

    asignaturas = cur.fetchall()

    sql = """
        SELECT
            m.matricula_id,
            a.nombre,
            s.nombre,
            m.created_at
        FROM matriculas m
        JOIN alumnos a
        ON m.alumno_id = a.alumno_id
        JOIN asignaturas s
        ON m.asignatura_id = s.asignatura_id
        WHERE CAST(m.created_at AS TEXT)
        ILIKE %s
        ORDER BY m.created_at DESC
        LIMIT %s OFFSET %s
    """

    cur.execute(
        sql,
        (
            f"%{fecha}%",
            limit,
            offset
        )
    )

    matriculas = cur.fetchall()

    conn.close()

    return render_template(
        "matriculas.html",
        alumnos=alumnos,
        asignaturas=asignaturas,
        matriculas=matriculas
    )

@matriculas_bp.route(
    "/matricula/add",
    methods=["POST"]
)
def add_matricula():

    alumno_id = request.form["alumno_id"]

    asignatura_id = request.form["asignatura_id"]

    conn = get_conn()

    cur = conn.cursor()

    try:

        cur.execute(
            """
            SELECT dinero
            FROM alumnos
            WHERE alumno_id=%s
            """,
            (alumno_id,)
        )

        dinero = cur.fetchone()[0]

        cur.execute(
            """
            SELECT precio,max_alumnos
            FROM asignaturas
            WHERE asignatura_id=%s
            """,
            (asignatura_id,)
        )

        asignatura = cur.fetchone()

        precio = asignatura[0]

        max_alumnos = asignatura[1]

        cur.execute(
            """
            SELECT COUNT(*)
            FROM matriculas
            WHERE asignatura_id=%s
            """,
            (asignatura_id,)
        )

        total = cur.fetchone()[0]

        if dinero < precio:

            conn.rollback()

            return "ERROR: dinero insuficiente"

        if total >= max_alumnos:

            conn.rollback()

            return "ERROR: asignatura llena"

        nuevo_dinero = dinero - precio

        cur.execute(
            """
            UPDATE alumnos
            SET dinero=%s
            WHERE alumno_id=%s
            """,
            (nuevo_dinero, alumno_id)
        )

        cur.execute(
            """
            INSERT INTO matriculas(
                alumno_id,
                asignatura_id
            )
            VALUES(%s,%s)
            """,
            (alumno_id, asignatura_id)
        )

        conn.commit()

    except Exception as e:

        conn.rollback()

        return f"ERROR TRANSACCION: {e}"

    finally:

        conn.close()

    return redirect("/matriculas")