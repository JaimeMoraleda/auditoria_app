from flask import Blueprint, render_template
from db import get_conn

vistas_bp = Blueprint(
    "vistas",
    __name__
)

@vistas_bp.route("/vista_matriculas")
def vista_matriculas():

    conn = get_conn()

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM vista_matriculas
        """
    )

    datos = cur.fetchall()

    conn.close()

    return render_template(
        "vista_matriculas.html",
        datos=datos
    )