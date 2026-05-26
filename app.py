from flask import Flask, render_template

from routes.profesores import profesores_bp
from routes.alumnos import alumnos_bp
from routes.asignaturas import asignaturas_bp
from routes.matriculas import matriculas_bp
from routes.vistas import vistas_bp
from routes.mapa import mapa_bp


app = Flask(__name__)

app.register_blueprint(profesores_bp)
app.register_blueprint(alumnos_bp)
app.register_blueprint(asignaturas_bp)
app.register_blueprint(matriculas_bp)
app.register_blueprint(vistas_bp)
app.register_blueprint(mapa_bp)

@app.route("/")
def index():

    return render_template("index.html")

app.run(debug=True)