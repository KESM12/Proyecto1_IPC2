class Disco: 
    def __init__(self,titulo, artista, pais, compania, precio, anio, ide):
        self.titulo = titulo
        self.artista = artista
        self.pais = pais
        self.compania = compania
        self.precio = precio
        self.anio = anio
        self.ide = ide
    
class Nodo: 
    def __init__(self,disco):
        self.disco = disco
        self.siguiente = None

class ListaDiscos:
    def __init__(self):
        self.primero = None
        self.contador = 0

    def Vacia(self):
        return self.primero == None

    def AregarDisco(self, titulo, artista, pais, compania, precio, anio):
        self.contador += 1
        if self.Vacia():
            self.primero = Nodo(Disco(titulo, artista, pais, compania, precio, anio, self.contador))
        else:
            primero = self.primero
            while primero.siguiente != None:
                primero = primero.siguiente
            primero.siguiente = Nodo(Disco(titulo, artista, pais, compania, precio, anio, self.contador))

        return Nodo(Disco(titulo, artista, pais, compania, precio, anio, self.contador))
    
    def imprimir(self):
        disco = []
        primero = self.primero
        while primero.siguiente!= None:
            print("===================================")
            print(f'Titulo Disco: {primero.disco.titulo}')
            print(f'Artista del Disco: {primero.disco.artista}')
            print(f'País del Disco: {primero.disco.pais}')
            print(f'Compania Disco: {primero.disco.compania}')
            print(f'Precio Disco: {primero.disco.precio}')
            print(f'Anio Disco: {primero.disco.anio}')
            disco.append(primero.disco)
            primero = primero.siguiente
        print("===================================")
        print(f'Titulo Disco: {primero.disco.titulo}')
        print(f'Artista del Disco: {primero.disco.artista}')
        print(f'País del Disco: {primero.disco.pais}')
        print(f'Compania Disco: {primero.disco.compania}')
        print(f'Precio Disco: {primero.disco.precio}')
        disco.append(primero.disco)
        return disco