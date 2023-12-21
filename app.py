

from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def inicio():  # put application's code here
    return render_template('Inicio.html')
@app.route('/ejercicio1',methods=['POST','GET'])
def formCompras():
    descuento = 0
    valorPintura = 9000
    totalSinDesc = 0
    totalConDesc = 0
    compras = {'nombre': "", 'edad': 0, 'cantTarros': 0}
    if(request.method=='POST'):
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantTarros = int(request.form['cantTarros'])
        totalSinDesc = (cantTarros * valorPintura)
        if edad >= 18 and edad <= 30:
            descuento = totalSinDesc * 15 / 100
        elif edad > 30:
            descuento = totalSinDesc * 25 / 100
        else:
            descuento = 0
        if descuento != 0:
            totalConDesc = totalSinDesc - descuento
        compras = {'nombre':nombre,'edad':edad,'cantTarros':cantTarros}

        return render_template('formulario1.html',compras=compras,nombre=nombre,totalConDesc=totalConDesc,totalSinDesc=totalSinDesc,descuento=descuento)

    return render_template('formulario1.html',compras=compras,totalConDesc=totalConDesc,totalSinDesc=totalSinDesc,descuento=descuento)

@app.route('/ejercicio2',methods=['POST','GET'])
def formSesion():
    usuarios = [{'nombre':"juan",'contrasena':"admin"},{'nombre':"pepe",'contrasena':"user"}]
    sesion = {"nombre":"","contrasena":""}
    mensaje = ""
    if(request.method=='POST'):
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']

        for user in usuarios:
            if(user['nombre'] == nombre and user['contrasena'] == contrasena):
                if(nombre.lower() == 'juan'):
                    mensaje = "Bienvenido administrador juan"
                    break
                else:
                    mensaje = "Bienvenido usuario pepe"
                    break
            else:
                mensaje = 'Usuario o contrasena incorrectos'

        sesion = {'nombre':nombre,'contrasena':contrasena}
        return render_template('formulario2.html',sesion = sesion,mensaje = mensaje)

    return render_template('formulario2.html',sesion=sesion,mensaje = mensaje)

if __name__ == '__main__':
    app.run(debug=True)
