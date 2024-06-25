#invocar a flask
from flask import Flask

#crear una app mediante la instancia
app=Flask(__name__)

#crear la ruta con su correspondientes funciones 

@app.route('/')
def hola_mundo():
    return f"Hola mundo"

@app.route('/ejecucion')
def mis_proyectos():
    return "Aqui se ejecuta el proyecto"

#Ejercutar nuestra app cuando ejecutemos este archivo run.py

if __name__=='__main__':
    app.run(debug=True)
