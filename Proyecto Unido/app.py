from msilib.schema import Directory
from flask import Flask, request, jsonify,send_from_directory
from flask.json import jsonify
from flask_cors import CORS
import LeerArchivo
from xml.dom import minidom
import xml.etree.ElementTree as ET
from graphviz import Digraph 
from xml import etree
import json
import os

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




@app.route('/eliminarEmpleado', methods=['POST'])
def eliminarEmpleado():
    empleadoEliminado=False
    empleados=minidom.parse("empleados.xml")
    todoempleados=empleados.documentElement
    idempleado= request.json['id']
    empleadoslista=todoempleados.getElementsByTagName('empleado')
    for empleado in empleadoslista:
        if empleado.attributes['id'].value ==idempleado:
            empleado.parentNode.removeChild(empleado)
            empleadoEliminado=True
    if empleadoEliminado==False:
        return jsonify(
            status=404,
            mensaje='No se encontro empleado para eliminar',
        )
    else:
        empleados.writexml(open("empleados.xml", 'w', encoding="utf-8"))
        return jsonify(
            status=200,
            mensaje='Empleado eliminado',
        )
@app.route('/discoTitulo', methods=['POST'])
def discoTitulo():
    discomostrado=False
    discos=minidom.parse("discos.xml")
    todosdiscos=discos.documentElement
    discotitulo= request.json['title']
    listadiscos=todosdiscos.getElementsByTagName('cd')
    for cd in listadiscos:
        if cd.getElementsByTagName('title')[0].childNodes[0].nodeValue ==discotitulo:
            artista=cd.getElementsByTagName('artist')[0].childNodes[0].nodeValue
            pais=cd.getElementsByTagName('country')[0].childNodes[0].nodeValue
            compania=cd.getElementsByTagName('company')[0].childNodes[0].nodeValue
            precio=cd.getElementsByTagName('price')[0].childNodes[0].nodeValue
            anio=cd.getElementsByTagName('year')[0].childNodes[0].nodeValue
            discomostrado=True
            return jsonify(
                mensaje="Usuario encontrado",
                artist=artista,
                country=pais,
                company=compania,
                price=precio,
                year=anio,
            )
    if discomostrado==False:
         return jsonify(
            status=404,
            mensaje='No se encontro disco',
        )
                
            
@app.route('/modificarDisco', methods=['POST'])
def modificarDisco():
    discomodificado=False
    discos=minidom.parse("discos.xml")
    todosdiscos=discos.documentElement
    listadiscos=todosdiscos.getElementsByTagName('cd')
    discotitulo= request.json['title']
    discoartista= request.json['artist']
    discopais= request.json['country']
    discocompania= request.json['company']
    discoprecio= request.json['price']
    discoanio= request.json['year']
    for cd in listadiscos:
       if cd.getElementsByTagName('title')[0].childNodes[0].nodeValue==discotitulo:
            cd.getElementsByTagName('artist')[0].childNodes[0].nodeValue=discoartista
            cd.getElementsByTagName('country')[0].childNodes[0].nodeValue=discopais
            cd.getElementsByTagName('company')[0].childNodes[0].nodeValue=discocompania
            cd.getElementsByTagName('price')[0].childNodes[0].nodeValue=discoprecio
            cd.getElementsByTagName('year')[0].childNodes[0].nodeValue=discoanio
            discomodificado=True
    if discomodificado==False:
        return jsonify(
            status=404,
            mensaje='No se encontro disco para modificar',
        )
    else:
        discos.writexml(open("discos.xml", 'w', encoding="utf-8"))
        return jsonify(
            status=200,
            mensaje='Disco modificado',
        )

@app.route('/reporteDiscos', methods=['GET'])
def reporteDiscos():
    discos=minidom.parse("discos.xml")
    tododiscos=discos.documentElement
    listadiscos=tododiscos.getElementsByTagName('cd')
    Discos = Digraph()
    contador = 0
    contador2 = 0
    Discos.node('Z', 'Desktop Records', shape='folder')
    while True:
        for cd in listadiscos:
            contador +=1
            Discos.node(f'A{contador}', 'cd: ' + cd.getElementsByTagName('title')[0].childNodes[0].nodeValue, shape='box3d')
            contador2 += 1
            Discos.node(f'B{contador2}', 'Artista: '+cd.getElementsByTagName('artist')[0].childNodes[0].nodeValue,shape='box')
            Discos.node(f'C{contador2}', 'País: '+cd.getElementsByTagName('country')[0].childNodes[0].nodeValue,shape='box')
            Discos.node(f'D{contador2}', 'Compañia: '+cd.getElementsByTagName('company')[0].childNodes[0].nodeValue,shape='box')
            Discos.node(f'E{contador2}', 'Precio: '+cd.getElementsByTagName('company')[0].childNodes[0].nodeValue,shape='box')
            Discos.node(f'E{contador2}', 'Año: '+cd.getElementsByTagName('year')[0].childNodes[0].nodeValue,shape='box')
                #------------------------------------------------
            Discos.edge(f'B{contador2}', f'C{contador2}')
            Discos.edge(f'C{contador2}', f'D{contador2}')
            Discos.edge(f'D{contador2}', f'E{contador2}')
                
            Discos.edge(f'A{contador}', f'B{contador2}')
            Discos.edge('Z', f'A{contador}')
        break
    contador += 1
    Discos.render('Reporte Discos',directory="C:/Users/SM/Desktop/IPC2 VACAS/Proyecto1_IPC2/DesktopWeb/Web/static", format='jpg', view=True)
    return 'Se genero el gráfico de discos.'


@app.route('/continente', methods=['POST'])
def continente():
    contienentemostrado=False
    contienente=[]
    mundo=minidom.parse("mundo.xml")
    todomundo=mundo.documentElement
    continentebuscado=request.json['continente']
    listacontinentes=todomundo.getElementsByTagName('continente')
    for continente in listacontinentes:
        if continente.attributes['name'].value==continentebuscado:
            listapaises=continente.getElementsByTagName('pais')
            for pais in listapaises:
                nombrepais=pais.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
                capital=pais.getElementsByTagName('capital')[0].childNodes[0].nodeValue
                moneda=pais.attributes['moneda'].value
                idioma=pais.getElementsByTagName('idioma')[0].childNodes[0].nodeValue
                poblacion=pais.getElementsByTagName('poblacion')[0].childNodes[0].nodeValue
                anipoblacion=pais.getElementsByTagName('poblacion')[0].attributes['year'].value
                unidad=pais.getElementsByTagName('poblacion')[0].attributes['unit'].value
                paisescontinente={"pais":nombrepais,"capital":capital,"moneda":moneda,"idioma":idioma,"poblacion":poblacion}
                contienente.append(paisescontinente)
                contienentemostrado=True
    if contienentemostrado==True:
        return jsonify(
        status=200,
        paises=contienente
        )
    else:
        return jsonify(
            status=404,
            mensaje='No se encontro continente',
        )

  



@app.route('/empleados', methods=['GET'])
def empleados():
    arbol=ET.parse('empleados.xml')
    raiz=arbol.getroot()
    cadena=escribirJSONempleado(raiz)
    objJson=json.loads(cadena)
    return objJson

def escribirJSONempleado(raiz_):
    cadena=""
    cadena+="{"+"\n"
    cadena+="\"empresa\":{"+"\n"
    cadena+="\"departamento\":["+"\n"
    cantDepartamentos=len(raiz_.findall('./departamento'))
    contadorDep=0
    for departamento in raiz_:
        contadorDep+=1  
        cadena+="{"+"\n"
        nombreDepartamento=departamento.attrib['departamento']
        cadena+="\"departamento\":"+"\""+nombreDepartamento+"\","+"\n"
        cadena+="\"empleado\":["+"\n"
        cantEmpleados=len(departamento.findall('./empleado'))
        contadorEmpleados=0
        for empleado in departamento:
            contadorEmpleados+=1 
            cadena+="{"+"\n"
            idEmpleado=empleado.attrib['id']
            nombreEmpleado=empleado.findall('nombre')[0].text
            cadena+="\"id\":"+"\""+idEmpleado+"\""+",\n"
            cadena+="\"nombre\":"+"\""+nombreEmpleado+"\""+"\n"
            cadena+="}"+"\n"
            if(contadorEmpleados<cantEmpleados):
                cadena+=","+"\n"
        cadena+="]"+"\n"
        cadena+="}"+"\n"
        if(contadorDep<cantDepartamentos):
            cadena+=","+"\n"
    cadena+="]"+"\n"
    cadena+="}"+"\n"
    cadena+="}"
    return cadena

@app.route('/modificarPais',methods=["POST"])
def modificarPais():
    jsonres=request.get_json()
    print(jsonres)
    continente_=jsonres['continente']
    nombre_=jsonres["nombre"]
    moneda_=jsonres['moneda']
    capital_=jsonres['capital']
    idioma_=jsonres['idioma']
    poblacion_=jsonres['poblacion']
    pobyear_ = jsonres['year']
    pobunit_ = jsonres['unit']
    
    arbol=ET.parse('mundo.xml')
    modificarPaises(arbol,continente_,nombre_,capital_,idioma_,poblacion_,moneda_,pobyear_,pobunit_)
    return 'Pais modificado con exito'

def modificarPaises(arbol_,continentebuscar_,nombrebuscar_,nuevacapital_,nuevoidioma_,nuevapoblacion_,nuevamoneda_,nuevoyear_,nuevaunit_):
    raiz_=arbol_.getroot()
    for mundo in raiz_:
        for continente in mundo:
            continenteactual=mundo.attrib['name']
            nombreactual = continente.findall('nombre')[0].text
            if(continenteactual==continentebuscar_) and (nombreactual == nombrebuscar_):
                continente.attrib['moneda']=nuevamoneda_
                continente.findall('capital')[0].text=nuevacapital_
                continente.findall('idioma')[0].text=nuevoidioma_
                continente.findall('poblacion')[0].text = nuevapoblacion_
                continente.findall('poblacion')[0].attrib['year'] = nuevoyear_
                continente.findall('poblacion')[0].attrib['unit'] = nuevaunit_
                arbol_.write('paises.xml',xml_declaration=True,encoding="utf-8")
                return
    print('No se encontro el Pais')


@app.route('/agregarEmpleado', methods=["POST"])
def agregarEmp():
    jsonres=request.get_json()
    print(jsonres)
    #departamento, id, nombre, puesto, salario
    departamento_ = jsonres['departamento']
    id_=jsonres['id']
    nombre_=jsonres["nombre"]
    puesto_=jsonres['puesto']
    salario_=jsonres['salario']
    
    arbol=ET.parse('empleados.xml')
    agregarempleado(arbol,departamento_,id_,nombre_,puesto_,salario_)
    return 'Empleado ha sido agregado'

def agregarempleado(arbol_,departamento,nuevoid,nuevonombre,nuevopuesto,nuevosalario):
        raiz_=arbol_.getroot()
        
        nuevodepto = ET.SubElement(raiz_,"departamento")
        nuevodepto.set('departamento', departamento)
        idnuevo = ET.SubElement(nuevodepto, "empleado")
        idnuevo.set('id', nuevoid)
        nombre = ET.SubElement(idnuevo, "nombre")
        nombre.text = str(nuevonombre)
        puesto = ET.SubElement(idnuevo, "puesto")
        puesto.text = str(nuevopuesto)
        salario = ET.SubElement(idnuevo, "salario")
        salario.text = str(nuevosalario)
        arbol_.write('empleados.xml',xml_declaration=True,encoding="utf-8")


@app.route('/discoArtista', methods=["POST"])
def discoArtista():
    xml_discos = ET.parse('discos.xml')
    xml_datos = xml_discos.getroot()
    artistaB = request.json['artist']
    artistanombre = (artistaB)
    Discos = []
    for catalog in xml_datos:
            catalog.findall('artist')
            artistA = catalog.findall('artist')[0].text
            artistA2 = artistA
            if artistA2 == artistanombre:
                tit = catalog.findall('title')[0].text
                art = catalog.findall('artist')[0].text
                coun = catalog.findall('country')[0].text
                comp = catalog.findall('company')[0].text
                pri = catalog.findall('price')[0].text
                year = catalog.findall('year')[0].text
                artistanom = {"title": tit, "artist": art, "country":coun, "company": comp, "price": pri, "year": year}
                Discos.append(artistanom)
    return jsonify(
        artistas = Discos
            )

@app.route('/paisMoneda', methods=["POST"])
def paisMoneda():
    xml_paises = ET.parse('mundo.xml')
    xml_datos = xml_paises.getroot()
    monedaE = request.json['moneda']
    monedaE2 = monedaE
    Paises = []
    for continente in xml_datos:
        lst_pais = continente.findall('pais')
        for pais in lst_pais:
            monedaA = pais.attrib['moneda']
            monedaa2 = monedaA
            if monedaa2 == monedaE2:
                cont = continente.attrib['name']
                mon = pais.attrib['moneda']
                nom = pais.findall('nombre')[0].text
                cap = pais.findall('capital')[0].text
                idio = pais.findall('idioma')[0].text
                pob = pais.findall('poblacion')[0].text
                monedaencontrada = {"continente": cont, "moneda": mon, "nombre": nom, "capital": cap, "idioma": idio, "poblacion": pob}
                Paises.append(monedaencontrada)
    return jsonify(
        monedas = Paises
            )



@app.route('/Bsueldo', methods=["POST"])
def Bsueldo():
    xml_empleados = ET.parse('empleados.xml')
    xml_datos = xml_empleados.getroot()
    salarioE = request.json['salario']
    salarioE2 = float(salarioE)
    Empleados = []
    for departamento in xml_datos:
        lst_emp = departamento.findall('empleado')
        for empleado in lst_emp:
            salarioA = empleado.findall('salario')[0].text
            salarioA2 = float(salarioA)
            if salarioA2 == salarioE2:
                dep = departamento.attrib['departamento']
                ident = empleado.attrib['id']
                nombre = empleado.findall('nombre')[0].text
                puesto = empleado.findall('puesto')[0].text
                salario = empleado.findall('salario')[0].text
                sueldousuario = {"departamento": dep, "id": ident, "nombre":nombre, "puesto": puesto, "salario": salario}
                Empleados.append(sueldousuario)
    return jsonify(
        empleados = Empleados
            )

@app.route('/ReporteEmpleados') #quemar la ruta para mostrarla en frontend
def ReporteEmpleados():
    xml_empleados = ET.parse('empleados.xml')
    xml_datos = xml_empleados.getroot()
    Empleados = Digraph()
    numero = 0
    numero2 = 0
    Empleados.node('Z', 'Desktop Records', shape='folder')
    while True:
        for dep in xml_datos:
            numero +=1
            Empleados.node(f'A{numero}', 'Departamento: ' + dep.attrib['departamento'], shape='box3d')
            lst_emp = dep.findall('empleado')
            for emp in lst_emp:
                numero2 += 1
                Empleados.node(f'B{numero2}', 'ID: '+emp.attrib['id'],shape='box')
                Empleados.node(f'C{numero2}', 'Nombre: '+emp.find('nombre').text,shape='box')
                Empleados.node(f'D{numero2}', 'Puesto: '+emp.find('puesto').text,shape='box')
                Empleados.node(f'E{numero2}', 'Salario: '+emp.find('salario').text,shape='box')
                #------------------------------------------------
                Empleados.edge(f'B{numero2}', f'C{numero2}')
                Empleados.edge(f'C{numero2}', f'D{numero2}')
                Empleados.edge(f'D{numero2}', f'E{numero2}')
                
                Empleados.edge(f'A{numero}', f'B{numero2}')
            Empleados.edge('Z', f'A{numero}')
        break
    numero += 1
    Empleados.render('Reporte Empleados', directory="C:/Users/SM/Desktop/IPC2 VACAS/Proyecto1_IPC2/DesktopWeb/Web/static", format='jpg', view=True)
    return 'Se genero el gráfico de empleados.'

@app.route('/ReporteRegiones') #quemar la ruta para mostrarla en frontend
def ReporteRegiones():
    xml_regiones = ET.parse('mundo.xml')
    xml_datos = xml_regiones.getroot()
    Regiones = Digraph()
    numero = 0
    numero2 = 0
    Regiones.node('Z', 'Desktop Records', shape='folder')
    while True:
        for reg in xml_datos:
            numero +=1
            Regiones.node(f'A{numero}', 'Continente: ' + reg.attrib['name'], shape='box3d')
            lst_emp = reg.findall('pais')
            for emp in lst_emp:
                numero2 += 1
                Regiones.node(f'B{numero2}', 'Moneda: '+emp.attrib['moneda'],shape='box')
                Regiones.node(f'C{numero2}', 'Nombre: '+emp.find('nombre').text,shape='box')
                Regiones.node(f'D{numero2}', 'Capital: '+emp.find('capital').text,shape='box')
                Regiones.node(f'E{numero2}', 'Idioma: '+emp.find('idioma').text,shape='box')
                Regiones.node(f'F{numero2}', 'PobYear: '+emp.findall('poblacion')[0].attrib['year'],shape='box')
                Regiones.node(f'G{numero2}', 'PobUnit: '+emp.findall('poblacion')[0].attrib['unit'],shape='box')
                Regiones.node(f'H{numero2}', 'Poblacion: '+emp.find('poblacion').text,shape='box')
                #------------------------------------------------
                Regiones.edge(f'B{numero2}', f'C{numero2}')
                Regiones.edge(f'C{numero2}', f'D{numero2}')
                Regiones.edge(f'D{numero2}', f'E{numero2}')
                Regiones.edge(f'E{numero2}', f'F{numero2}')
                Regiones.edge(f'F{numero2}', f'G{numero2}')
                Regiones.edge(f'G{numero2}', f'H{numero2}')
                Regiones.edge(f'A{numero}', f'B{numero2}')
            Regiones.edge('Z', f'A{numero}')
        break
    numero += 1
    Regiones.render('Reporte Regiones',directory="C:/Users/SM/Desktop/IPC2 VACAS/Proyecto1_IPC2/DesktopWeb/Web/static", format='jpg', view=True)
    return 'Se genero el gráfico de Regiones.'

@app.route('/yearDisco', methods=["POST"])
def yearDisco():
    xml_discos = ET.parse('discos.xml')
    xml_datadisc = xml_discos.getroot()
    yearDiscBR = request.json['year']
    yearDiscB = int(yearDiscBR)
    Discos = []
    for disc in xml_datadisc:
        yearDiscAR = disc.findall('year')[0].text
        yearDiscA = int(yearDiscAR)
        if (yearDiscA == yearDiscB):
            titulo = disc.findall('title')[0].text
            artista = disc.findall('artist')[0].text
            ciudad = disc.findall('country')[0].text
            compania = disc.findall('company')[0].text
            precio = disc.findall('price')[0].text
            anio = disc.findall('year')[0].text
            discosEncontrados = {"titulo":titulo, "artista": artista, "ciudad": ciudad, "compania": compania, "precio": precio, "anio":anio}
            Discos.append(discosEncontrados)
    return jsonify(
        discos = Discos
    )

@app.route('/eliminarDisco', methods=["POST"])
def eliminarDisco():
    xml_discos = ET.parse('discos.xml')
    xml_datadisc = xml_discos.getroot()
    TituloB = request.json['title']
    Discos = []
    for disc in xml_datadisc:
        TituloA = disc.findall('title')[0].text
        titulo = disc.findall('title')[0].text
        artista = disc.findall('artist')[0].text
        ciudad = disc.findall('country')[0].text
        compania = disc.findall('company')[0].text
        precio = disc.findall('price')[0].text
        anio = disc.findall('year')[0].text
        discosEncontrados = {"titulo":titulo, "artista": artista, "ciudad": ciudad, "compania": compania, "precio": precio, "anio":anio}
        Discos.append(discosEncontrados)
        if (TituloA == TituloB):
            titulo = disc.findall('title')[0].text
            artista = disc.findall('artist')[0].text
            ciudad = disc.findall('country')[0].text
            compania = disc.findall('company')[0].text
            precio = disc.findall('price')[0].text
            anio = disc.findall('year')[0].text
            discosEncontrados = {"titulo":titulo, "artista": artista, "ciudad": ciudad, "compania": compania, "precio": precio, "anio":anio}
            Discos.remove(discosEncontrados)
            xml_datadisc.remove(disc)
            xml_discos.write('Discos.xml')
    return jsonify(
        discos = Discos
    )

@app.route('/Paises')
def Paises():
    xml_mundo = ET.parse('mundo.xml')
    xml_datamundo = xml_mundo.getroot()
    Paises = []
    for continente in xml_datamundo:
        conti = continente.attrib['name']
        lst_paises = continente.findall('pais')
        for pais in lst_paises:
            pa = pais.attrib['moneda']
            nom = pais.findall('nombre')[0].text
            capi = pais.findall('capital')[0].text
            idi = pais.findall('idioma')[0].text
            pobyear = pais.findall('poblacion')[0].attrib['year']
            pobunit = pais.findall('poblacion')[0].attrib['unit']
            pob = pais.findall('poblacion')[0].text
            paisesEnc = {"continente":conti, "moneda": pa, "nombre": nom, "capital": capi, "idioma": idi, "Poblacion" : pob, "PobYear": pobyear, "PobUnit": pobunit}
            Paises.append(paisesEnc)
    return jsonify(
        paises = Paises
    )

@app.route('/agregarPais', methods=["POST"])
def agregarPais():
    xml_mundo = ET.parse('mundo.xml')
    xml_datamundo = xml_mundo.getroot()
    NuevoConti = request.json['continente']
    NuevoMoneda = request.json['moneda'] #pais
    NuevoNombre = request.json['nombre']
    NuevoCapital = request.json['capital']
    NuevoIdioma = request.json['idioma']
    NuevoPoblacion = request.json['poblacion'] 
    NuevoPobYear = request.json['PobYear']
    NuevoPobUnit = request.json['PobUnit']
    Paises = []
    paisesnuevos = ET.Element('mundo')
    for continente in xml_datamundo:
        conti = continente.attrib['name']
        lst_paises = continente.findall('pais')
        for pais in lst_paises:
            pa = pais.attrib['moneda']
            nom = pais.findall('nombre')[0].text
            capi = pais.findall('capital')[0].text
            idi = pais.findall('idioma')[0].text
            pob = pais.findall('poblacion')[0].text
            pobyear = pais.findall('poblacion')[0].attrib['year']
            pobunit = pais.findall('poblacion')[0].attrib['unit']
            paisesEnc = {"continente":conti, "moneda": pa, "nombre": nom, "capital": capi, "idioma": idi, "Poblacion" : pob, "PobYear": pobyear, "PobUnit": pobunit}
            Paises.append(paisesEnc)
            continentenew = ET.SubElement(paisesnuevos, "continente")
            paisnew = ET.SubElement(continentenew, 'pais')
            nombre2 = ET.SubElement(paisnew, 'nombre')
            capital = ET.SubElement(paisnew, 'capital')
            idioma = ET.SubElement(paisnew, 'idioma')
            poblacion = ET.SubElement(paisnew, 'poblacion')
            continentenew.set('name',f'{conti}')
            paisnew.set('moneda', f'{pa}')
            poblacion.set('year', f'{pobyear}')
            poblacion.set('unit', f'{pobunit}')
            nombre2.text = f'{nom}'
            capital.text = f'{capi}'
            idioma.text = f'{idi}'
            poblacion.text = f'{pob}'
            #-----------------------------
    continentenew2 = ET.SubElement(paisesnuevos, "continente")
    paisnew = ET.SubElement(continentenew2, 'pais')
    nombre2 = ET.SubElement(paisnew, 'nombre')
    capital = ET.SubElement(paisnew, 'capital')
    idioma = ET.SubElement(paisnew, 'idioma')
    poblacion = ET.SubElement(paisnew, 'poblacion')
    continentenew2.set('name',f'{NuevoConti}')
    paisnew.set('moneda', f'{NuevoMoneda}')
    poblacion.set('year', f'{NuevoPobYear}')
    poblacion.set('unit', f'{NuevoPobUnit}')
    nombre2.text = f'{NuevoNombre}'
    capital.text = f'{NuevoCapital}'
    idioma.text = f'{NuevoIdioma}'
    poblacion.text = f'{NuevoPoblacion}'
    #------------------------------
    #print(mydata)
    xml_mundo = ET.ElementTree(paisesnuevos)
    xml_mundo.write('mundo.xml')
    parser = etree.XMLParser(remove_blank_text=True,compact=True)
    mundoxml = etree.parse("Mundo.xml", parser=parser)
    #equipoXML = arbolXML.getroot()
    mundoxml.write("mundo.xml", pretty_print=True,encoding="utf-8")
    paisNuevo = {"continente":NuevoConti, "moneda": NuevoMoneda, "nombre": NuevoNombre, "capital": NuevoCapital, "idioma": NuevoIdioma, "Poblacion" : NuevoPoblacion, "PobYear": NuevoPobYear, "PobUnit": NuevoPobUnit}
    Paises.append(paisNuevo)
    return jsonify(
        paises = Paises
    )

#METODO PRINCIPAL
if(__name__=='__main__'):
    app.run(host="0.0.0.0",port=7000,debug=False)