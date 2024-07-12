#invocar a flask
from flask import Flask,render_template

#crear una app mediante la instancia
app=Flask(__name__)

#crear la ruta con su correspondientes funciones 

#Inicio
@app.route('/',methods=['GET'])
def hola_mundo():
    return render_template('index.html')

#formulario
@app.route('/formulario',methods=['GET'])  #indicamos el metodo GET
def formulario():
    return render_template('formulario.html')

# mis proyectos
@app.route('/mis_proyectos', methods=['GET'])
def mis_proyectos():
    return "Aqui se ejecuta el proyecto"


#Ejercutar nuestra app cuando ejecutemos este archivo run.py

if __name__=='__main__':
    app.run(debug=True)
