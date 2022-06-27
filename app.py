from flask import Flask, request, jsonify
from flask_cors import CORS
import LeerArchivo


app = Flask(__name__)
CORS(app)

@app.route("/cargarDatosEmpleados", methods=["POST"])
def CargarDatos():
    datos = request.data
    LeerArchivo.cargarDatosEmpleados(datos)
    return datos

@app.route("/empleadoNombre", methods=["POST"])
def empleadoNombre():
    aux = []
    data = request.get_json()
    nombre = data["nombre"]
    empleados = LeerArchivo.listaE.BuscarNombre(nombre)
    for empleado in empleados:
        aux.append({"ID empleado": empleado.ide, "Nombre empleado": empleado.nombre, "Puesto empleado": empleado.puesto, "Salario empleado": empleado.salario, "Departamento empleado": empleado.depto})
    return jsonify(aux)

@app.route("/empleadoDepartamento", methods=["POST"])
def modificarEmpleado ():
    aux = []
    data = request.get_json()
    departamento = data["departamento"]
    empleados = LeerArchivo.listaE.Buscardepto(departamento)
    for empleado in empleados:
        aux.append({"ID empleado": empleado.ide, "Nombre empleado": empleado.nombre, "Puesto empleado": empleado.puesto, "Salario empleado": empleado.salario, "Departamento empleado": empleado.depto})
    return jsonify(aux)

@app.route("/modificarEmpleado", methods=["POST"])
def empleadoDepartamento():
    aux = []
    data = request.get_json()
    IDe = data["ID"]
    nombreN = data["nombre"]
    puestoN = data["puesto"]
    salarioN = data["salario"]
    empleadoN = LeerArchivo.listaE.Modificar(IDe, nombreN, puestoN,salarioN)
    aux.append({"ID empleado": empleadoN.ide, "Nombre empleado": empleadoN.nombre, "Puesto empleado": empleadoN.puesto, "Salario empleado": empleadoN.salario, "Departamento empleado": empleadoN.depto})
    return jsonify(aux)

@app.route("/Discos", methods=["GET"])
def cargarDatosDiscos():
    aux = []
    datos = request.data
    LeerArchivo.cargarDatosDiscos(datos)
    discos = LeerArchivo.listaD.imprimir()
    for disco in discos:
        aux.append({"Titulo": disco.titulo, "Artista": disco.artista, "Pais": disco.pais, "Precio": disco.precio,"Año": disco.anio})
    return jsonify(aux)

@app.route("/agregarDisco", methods=["POST"])
def agregarDisco():
    aux = []
    data = request.get_json()
    titulo = data["titulo"]
    artista = data["artista"]
    pais = data["pais"]
    precio = data["precio"]
    compania = data["compania"]
    año = data["año"]
    discoN = LeerArchivo.listaD.AregarDisco(titulo, artista, pais,compania,precio,año)
    aux.append({"Titulo": titulo, "Artista": artista, "Pais": pais, "Compañia":compania, "Precio":precio, "Año":año})
    return jsonify(aux)

@app.route("/cargarDatosPaises", methods=["POST"])
def cargarDatosPaises():
    datos = request.data
    LeerArchivo.cargarDatosPaises(datos)
    return datos

@app.route("/paisIdioma", methods=["POST"])
def paisIdioma ():
    aux = []
    data = request.get_json()
    idioma = data["idioma"]
    paises = LeerArchivo.listaP.BuscarIdioma(idioma)
    for pais in paises:
        aux.append({"Continente": pais.continente, "Moneda": pais.moneda, "Nombre": pais.nombre, "Capital": pais.capital, "Idioma" : pais.idioma, "Año Poblacion" : pais.poblacionAño, "Unidad de medida" : pais.poblacionUnidad, "Cantidad de Poblacion" : pais.poblacion})
    return jsonify(aux)

