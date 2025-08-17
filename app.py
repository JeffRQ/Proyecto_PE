from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Bienvenido a mi pagina web"

@app.route('/usuarios/<Jorge>')
def about(Jorge):
    return f"Hola: {Jorge}!"

@app.route('/Jefferson')
def Jefferson():
    return "Jefferson"

@app.route('/Ramirez')
def Ramirez():
    return "Ramirez"

@app.route('/Quimi')
def Quimi():
    return "Quimi"

if __name__ == '__main__':
    app.run(debug=True)