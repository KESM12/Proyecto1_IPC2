from xml.dom import minidom
from flask import Flask, request,jsonify,send_from_directory
from flask.json import jsonify
import os
import xml.etree.ElementTree as ET
app = Flask(__name__)
ContadorDiscos=0

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
    global ContadorDiscos
    ruta=os.getcwd()
    discos=minidom.parse("discos.xml")
    tododiscos=discos.documentElement
    graficadiscos=""
    graficadiscos+="digraph G { \n"
    graficadiscos+="node[shape=box] \n"
    graficadiscos+="nodoRaiz[label=\"Catalogo\"] \n"
    discograficar=tododiscos.getElementsByTagName('cd')
    for disco in discograficar:
        NodoDisco="cd"+str(ContadorDiscos)
        ContadorDiscos+=1
        graficadiscos+=NodoDisco+"[label=\" CD \"] \n"
        graficadiscos+="nodoRaiz ->"+NodoDisco+"\n"
        NodoTitulo=NodoDisco+"title"
        NodoArtista=NodoDisco+"Artista"
        NodoPais=NodoDisco+"pais"
        NodoCompania=NodoDisco+"compania"
        NodoPrecio=NodoDisco+"precio"
        Nodoanio=NodoDisco+"anio"
        AuxTitulo=disco.getElementsByTagName('title')[0].childNodes[0].nodeValue
        AuxArtista=disco.getElementsByTagName('artist')[0].childNodes[0].nodeValue
        AuxPais=disco.getElementsByTagName('country')[0].childNodes[0].nodeValue
        AuxCompania=disco.getElementsByTagName('company')[0].childNodes[0].nodeValue
        AuxPrecio=disco.getElementsByTagName('price')[0].childNodes[0].nodeValue
        AuxAnio=disco.getElementsByTagName('year')[0].childNodes[0].nodeValue
        Titulo=AuxTitulo.replace('"','\\"')
        Artista=AuxArtista.replace('"','\\"')
        Pais=AuxPais.replace('"','\\"')
        Compania=AuxCompania.replace('"','\\"')
        Precio=AuxPrecio.replace('"','\\"')
        Anio=AuxAnio.replace('"','\\"')
        graficadiscos+=NodoTitulo+"[label=\"Titulo: "+Titulo+" \"] \n"
        graficadiscos+=NodoArtista+"[label=\"Artista: "+Artista+" \"] \n"
        graficadiscos+=NodoPais+"[label=\"País: "+Pais+" \"] \n"
        graficadiscos+=NodoCompania+"[label=\"Compañia: "+Compania+" \"] \n"
        graficadiscos+=NodoPrecio+"[label=\"Precio: "+Precio+" \"] \n"
        graficadiscos+=Nodoanio+"[label=\"Año: "+Anio+" \"] \n"
        graficadiscos+=NodoDisco+"->"+NodoTitulo+"\n"
        graficadiscos+=NodoTitulo+"->"+NodoPais+"\n"
        graficadiscos+=NodoTitulo+"->"+NodoArtista+"\n"
        graficadiscos+=NodoTitulo+"->"+NodoCompania+"\n"
        graficadiscos+=NodoTitulo+"->"+NodoPrecio+"\n"
        graficadiscos+=NodoTitulo+"->"+Nodoanio+"\n"
    graficadiscos+="}"
    DiscosDot=open("Discosdot.dot",'w',encoding="utf-8")
    DiscosDot.write(graficadiscos)
    DiscosDot.close()
    comando= "dot -Tjpg Discosdot.dot -o ReporteDiscos.jpg"
    os.system(comando)
    return send_from_directory(ruta,path="ReporteDiscos.jpg", as_attachment=False)
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

@app.route('/reporteRegiones', methods=['GET'])
def reporteRegiones():
    mundo=minidom.parse("mundo.xml")
    todomundo=mundo.documentElement
    graficaregiones=""
    graficaregiones+="digraph G { \n"
    graficaregiones+="node[shape=box] \n"
    graficaregiones+="nodoRaiz[label=\"Empresa\"] \n"
    continentesgraficar=todomundo.getElementsByTagName('continente')
    for continente in continentesgraficar:
        Nodoregion="continente"+continente.attributes['name'].value
        graficaregiones+=Nodoregion+"[label=\" Continente: "+continente.attributes['name'].value+"\"] \n"
        graficaregiones+="nodoRaiz ->"+Nodoregion+"\n"
        listapaises=continente.getElementsByTagName('pais')
        for pais in listapaises:
            auxnombrepais=pais.getElementsByTagName('nombre')[0].childNodes[0].nodeValue
            nombrepais=auxnombrepais.replace('"','\\"')
            NodoID="ID"+nombrepais
            graficaregiones+=NodoID+"[label=\"Pais: "+nombrepais+" \"] \n"
            graficaregiones+=Nodoregion+"->"+NodoID+"\n"
            NodoCapitalPais=NodoID+"capital"
            NodoMonedaPais=NodoID+"moneda"
            NodoIdiomaPais=NodoID+"idioma"
            NodoPoblacionPais=NodoID+"poblacion"
            AuxCapitalPais=pais.getElementsByTagName('capital')[0].childNodes[0].nodeValue
            AuxMonedaPais=pais.attributes['moneda'].value
            AuxIdiomaPais=pais.getElementsByTagName('idioma')[0].childNodes[0].nodeValue
            AuxPoblacionPais=pais.getElementsByTagName('poblacion')[0].childNodes[0].nodeValue
            AuxAnioPais=pais.getElementsByTagName('poblacion')[0].attributes['year'].value
            AuxUnidadPais=pais.getElementsByTagName('poblacion')[0].attributes['unit'].value
            CapitalPais=AuxCapitalPais.replace('"','\\"')
            MonedaPais=AuxMonedaPais.replace('"','\\"')
            IdiomaPais=AuxIdiomaPais.replace('"','\\"')
            PoblacionPais=AuxPoblacionPais.replace('"','\\"')
            AnioPais=AuxAnioPais.replace('"','\\"')
            UnidadPais=AuxUnidadPais.replace('"','\\"')
            if UnidadPais=="thousands" or UnidadPais=="\'thousands\'":
                UnidadPais="miles"
            elif UnidadPais=="millions" or UnidadPais=="\'millions\'":
                UnidadPais="millones"
            graficaregiones+=NodoCapitalPais+"[label=\"Capital: "+CapitalPais+" \"] \n"
            graficaregiones+=NodoMonedaPais+"[label=\"Moneda: "+MonedaPais+" \"] \n"
            graficaregiones+=NodoIdiomaPais+"[label=\"Idioma: "+IdiomaPais+" \"] \n"
            graficaregiones+=NodoPoblacionPais+"[label=\"Población: "+PoblacionPais+" "+UnidadPais+" (hasta el año "+AnioPais+" ) \"] \n"
            graficaregiones+=NodoID+"->"+NodoCapitalPais+"\n"
            graficaregiones+=NodoID+"->"+NodoMonedaPais+"\n"
            graficaregiones+=NodoID+"->"+NodoIdiomaPais+"\n"
            graficaregiones+=NodoID+"->"+NodoPoblacionPais+"\n"
    graficaregiones+="}"
    Dot=open("mundo.dot",'w',encoding="utf-8")
    Dot.write(graficaregiones)
    Dot.close()
    comando= "dot -Tjpg mundo.dot -o ReporteMundo.jpg"
    os.system(comando)
    ruta=os.getcwd()
    return send_from_directory(ruta,path="ReporteMundo.jpg", as_attachment=False)            

                
if __name__=='__main__':
    app.run(debug=True, port=4000)