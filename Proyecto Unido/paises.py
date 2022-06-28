class Pais: 
    def __init__(self,continente, moneda, nombre, capital, idioma, poblacionAño, poblacionUnidad, poblacion):
        self.continente = continente
        self.moneda = moneda
        self.nombre = nombre
        self.capital = capital
        self.idioma = idioma
        self.poblacionAño = poblacionAño
        self.poblacionUnidad = poblacionUnidad
        self.poblacion = poblacion
    
class Nodo: 
    def __init__(self,pais):
        self.pais = pais
        self.siguiente = None

class ListaPaises:
    def __init__(self):
        self.primero = None
        self.contador = 0

    def Vacia(self):
        return self.primero == None

    def AregarPais(self, continente, moneda, nombre, capital, idioma, poblacionAño, poblacionUnidad, poblacion):
        self.contador += 1
        if self.Vacia():
            self.primero = Nodo(Pais(continente, moneda, nombre, capital, idioma, poblacionAño, poblacionUnidad, poblacion))
        else:
            primero = self.primero
            while primero.siguiente != None:
                primero = primero.siguiente
            primero.siguiente = Nodo(Pais(continente, moneda, nombre, capital, idioma, poblacionAño, poblacionUnidad, poblacion))

        return Nodo(Pais(continente, moneda, nombre, capital, idioma, poblacionAño, poblacionUnidad, poblacion))
    
    def BuscarIdioma(self, idioma):
        paises = []
        actual = self.primero
        print('¡Paise(s) econtrado(s)!')
        contadorDiscos = 0
        while actual.siguiente != None:               
            if actual.pais.idioma == (idioma):
                contadorDiscos += 1
                print('_________________________________________________')
                print(f'Continente: {actual.pais.continente}')
                print(f'Moneda: {actual.pais.moneda}')
                print(f'Nombre: {actual.pais.nombre}')
                print(f'capital: {actual.pais.capital}')
                print(f'Idioma: {actual.pais.idioma}')
                print(f'Año Poblacion: {actual.pais.poblacionAño}')
                print(f'Unidad de medida: {actual.pais.poblacionUnidad}')
                print(f'Cantidad de Poblacion: {actual.pais.poblacion}')
                paises.append(actual.pais)
            actual = actual.siguiente             
        if actual.pais.idioma == (idioma):
            contadorDiscos += 1
            print('_________________________________________________')
            print(f'Continente: {actual.pais.continente}')
            print(f'Moneda: {actual.pais.moneda}')
            print(f'Nombre: {actual.pais.nombre}')
            print(f'capital: {actual.pais.capital}')
            print(f'Idioma: {actual.pais.idioma}')
            print(f'Año Poblacion: {actual.pais.poblacionAño}')
            print(f'Unidad de medida: {actual.pais.poblacionUnidad}')
            print(f'Cantidad de Poblacion: {actual.pais.poblacion}')
            paises.append(actual.pais)
        print(f'Cantidad de paises encontrados: {contadorDiscos}')
        return paises
    
    def imprimir(self):
        pais = []
        actual = self.primero
        while actual.siguiente!= None:
            print("===================================")
            print(f'Continente: {actual.pais.continente}')
            print(f'Moneda: {actual.pais.moneda}')
            print(f'Nombre: {actual.pais.nombre}')
            print(f'capital: {actual.pais.capital}')
            print(f'Idioma: {actual.pais.idioma}')
            print(f'Año Poblacion: {actual.pais.poblacionAño}')
            print(f'Unidad de medida: {actual.pais.poblacionUnidad}')
            print(f'Cantidad de Poblacion: {actual.pais.poblacion}')
            pais.append(actual.pais)
            actual = actual.siguiente
        print("===================================")
        print(f'Continente: {actual.pais.continente}')
        print(f'Moneda: {actual.pais.moneda}')
        print(f'Nombre: {actual.pais.nombre}')
        print(f'capital: {actual.pais.capital}')
        print(f'Idioma: {actual.pais.idioma}')
        print(f'Año Poblacion: {actual.pais.poblacionAño}')
        print(f'Unidad de medida: {actual.pais.poblacionUnidad}')
        print(f'Cantidad de Poblacion: {actual.pais.poblacion}')
        pais.append(actual.pais)
        return pais