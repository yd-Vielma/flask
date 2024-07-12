#invocar a flask
from flask import Flask,render_template

#crear una app mediante la instancia
app=Flask(__name__)

#crear la ruta con su correspondientes funciones 

#inicio
@app.route('/',methods=['GET'])
def index():
    return render_template('/index.html')

#mis proyectos
@app.route('/proyectos',methods=['GET'])  #indicamos el metodo GET
def mis_proyectos():
    return "Aqui se ejecuta el proyecto"

#formulario
@app.route('/formulario', methods=['GET','POST'])
def formulario_registro():
    return render_template('formulario.html')

#vias de contacto
@app.route('/contactos.html',methods=['GET'])
def contactos():
    return render_template('contacto.html')


if __name__=='__main__':
    app.run(debug=True)
