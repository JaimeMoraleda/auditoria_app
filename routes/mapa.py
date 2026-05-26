from flask import Blueprint, render_template
from psycopg.rows import dict_row
import psycopg

mapa_bp = Blueprint("mapa", __name__)

conninfo = "host=localhost port=5434 dbname=auditoria_db user=postgres password=1234"

@mapa_bp.route("/mapa")
def mapa():

    conn = psycopg.connect(conninfo, row_factory=dict_row)
    cur = conn.cursor()

    cur.execute("""
        SELECT
            alumno_id,
            nombre,
            ST_Y(ubicacion) AS lat,
            ST_X(ubicacion) AS lon
        FROM alumnos
        WHERE ubicacion IS NOT NULL;
    """)

    alumnos = cur.fetchall()

    cur.execute("""
        SELECT
            asignatura_id,
            nombre,
            ST_AsGeoJSON(aula) AS geojson
        FROM asignaturas
        WHERE aula IS NOT NULL;
    """)

    asignaturas = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "mapa.html",
        alumnos=alumnos,
        asignaturas=asignaturas
    )