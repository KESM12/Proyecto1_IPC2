from flask import Flask, jsonify, request
from flask_cors import CORS
import xml.etree.ElementTree as ET
import json
from graphviz import Digraph 
import pandas as pd


app = Flask(__name__)
CORS(app)

@app.route('/')
def inicio():
    return 'Prueba del server'

@app.route('/Bsueldo', methods=["POST"])
def Bsueldo():
    xml_empleados = ET.parse('Empleados.xml')
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
    xml_empleados = ET.parse('Empleados.xml')
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
    Empleados.render('Reporte Empleados', format='jpg', view=True)
    return 'Se genero el gráfico de empleados.'

@app.route('/yearDisco', methods=["POST"])
def yearDisco():
    xml_discos = ET.parse('Discos.xml')
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
    xml_discos = ET.parse('Discos.xml')
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
    xml_mundo = ET.parse('Mundo.xml')
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
    xml_mundo = ET.parse('Mundo.xml')
    xml_datamundo = xml_mundo.getroot()
    NuevoConti = request.json['continente']
    newCoti = ET.Element(NuevoConti)
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
            pobyear = pais.findall('poblacion')[0].attrib['year']
            pobunit = pais.findall('poblacion')[0].attrib['unit']
            pob = pais.findall('poblacion')[0].text
            paisesEnc = {"continente":conti, "moneda": pa, "nombre": nom, "capital": capi, "idioma": idi, "Poblacion" : pob, "PobYear": pobyear, "PobUnit": pobunit}
            Paises.append(paisesEnc)
            #paisesnuevos = ET.Element('mundo')
            #continentenew = ET.SubElement(paisesnuevos, "continente")
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
            #-----------------------------
    paisnew = ET.SubElement(continentenew, 'pais')
    nombre2 = ET.SubElement(paisnew, 'nombre')
    capital = ET.SubElement(paisnew, 'capital')
    idioma = ET.SubElement(paisnew, 'idioma')
    poblacion = ET.SubElement(paisnew, 'poblacion')
    continentenew.set('name',f'{NuevoConti}')
    paisnew.set('moneda', f'{NuevoMoneda}')
    poblacion.set('year', f'{NuevoPobYear}')
    poblacion.set('unit', f'{NuevoPobUnit}')
    nombre2.text = f'{NuevoNombre}'
    capital.text = f'{NuevoCapital}'
    idioma.text = f'{NuevoIdioma}'
    poblacion.text = f'{NuevoPoblacion}'
    #------------------------------
    mydata = str(ET.tostring(paisesnuevos))
    #print(mydata)
    actualizacion = open("Mundo2.xml", "w")
    actualizacion.write(mydata)
    paisNuevo = {"continente":NuevoConti, "moneda": NuevoMoneda, "nombre": NuevoNombre, "capital": NuevoCapital, "idioma": NuevoIdioma, "Poblacion" : NuevoPoblacion, "PobYear": NuevoPobYear, "PobUnit": NuevoPobUnit}
    Paises.append(paisNuevo)
    return jsonify(
        paises = Paises
    )

@app.route('/nose') #usar este codigo para crear el nuevo xml alv

def nose():
    # create the file structure
    data = ET.Element('data') #primer campo
    items = ET.SubElement(data, 'items')   #segundo campo                           
    item3 = ET.SubElement(items, 'item') #continente
    item4 = ET.SubElement(items, 'item') #pais (moneda)
    item3.set('name','item1') #atributos #contienen
    item4.set('name','item2') #atributos
    item3.text="item1abc" #texto a quemar
    item4.text="item2abc" #texto a quemar

    # create a new XML file with the results
    mydata = ET.tostring(data)
    mydata2 = str(mydata)
    myfile = open("items2.xml", "a")
    myfile.write(mydata2)
    return 'alch'


#METODO PRINCIPAL
if(__name__=='__main__'):
    app.run(host="0.0.0.0",port=8000,debug=False)