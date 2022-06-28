from re import I
import xml.etree.ElementTree as ET
from empleados import ListaEmpleados
from discos import ListaDiscos
from paises import ListaPaises

listaD = ListaDiscos()
listaE = ListaEmpleados()
listaP = ListaPaises()

global año 
def cargarDatosEmpleados(texto):
    xml_data = ET.ElementTree(ET.fromstring(texto))
    depto = xml_data.findall('departamento')
    for emp in depto: 
        NombreDepto= emp.get('departamento')
        empleado = emp.findall('empleado')
        #print(f'Departamento: {NombreDepto}'
        for dato in empleado:
            id = dato.get('id')
            nombre = dato.find('nombre').text
            puesto = dato.find('puesto').text
            salario = dato.find('salario').text
            #print(f'-ID: {id} -Nombre: {nombre} -Puesto: {puesto} -Salario {salario}')
            listaE.AregarEmpleado(nombre,puesto,salario,id,NombreDepto)
    listaE.imprimir()

def cargarDatosPaises(texto):
    xml_data = ET.ElementTree(ET.fromstring(texto))
    continente = xml_data.findall('continente')
    for paises in continente:
        nombreCon = paises.get('name')
        for pais in paises:
            moneda = pais.get('moneda')
            nombre = pais.find('nombre').text
            capital = pais.find('capital').text
            idioma = pais.find('idioma').text
            poblacion = pais.find('poblacion').text
            poblacionn = xml_data.findall('poblacion')
            '''for datosP in poblacionn:
                año = datosP.get('year')
                unidad = datosP.get('unit')'''
            listaP.AregarPais(nombreCon,moneda,nombre, capital, idioma,1,1,poblacion)
    listaP.imprimir()        



def cargarDatosDiscos(texto):
    xml_data = ET.ElementTree(ET.fromstring(texto))
    cd = xml_data.findall('cd')
    for cds in cd:
        titulo = cds.find('title').text
        titulon = titulo.replace('"','')
        artista = cds.find('artist').text
        pais = cds.find('country').text
        compania = cds.find('company').text
        precio = cds.find('price').text
        anio = cds.find('year').text
        listaD.AregarDisco(titulon,artista,pais,compania,precio,anio)
    return listaD.AregarDisco(titulon,artista,pais,compania,precio,anio)
    #listaD.imprimir()