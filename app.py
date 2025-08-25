from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

BRAND = {
    "name": "Teiprometal",
    "slogan": "Soluciones metalmecánicas a la medida",
    "tagline": "Diseño, fabricación y mantenimiento industrial",
    "contact": {"email": "contacto@teiprometal.ec", "phone": "+593 99 999 9999", "city": "Camilo Ponce Enríquez, Azuay"},
    "services": [
        "Corte y doblado de lámina",
        "Soldadura MIG/TIG y arco",
        "Estructuras metálicas",
        "Mantenimiento industrial",
        "Diseño CAD y prototipado"
    ]
}

@app.context_processor
def inject_globals():
    return {"brand": BRAND, "current_year": datetime.now().year, "request": request}

@app.route("/")
def index():
    highlights = [
        {"title": "Entrega a tiempo", "desc": "Planificación y control de producción."},
        {"title": "Calidad verificada", "desc": "Procedimientos y pruebas NDT."},
        {"title": "CAD/CAM", "desc": "Planos y renders para aprobación."}
    ]
    return render_template("index.html", highlights=highlights)

@app.route("/about")
def about():
    mission = "Brindar soluciones metalmecánicas confiables."
    vision = "Ser referentes regionales en innovación y calidad."
    values = ["Seguridad", "Calidad", "Cumplimiento", "Transparencia", "Servicio"]
    return render_template("about.html", mission=mission, vision=vision, values=values)

@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f"¡Bienvenido a {BRAND['name']}, {nombre}!"

if __name__ == "__main__":
    app.run(debug=True)

