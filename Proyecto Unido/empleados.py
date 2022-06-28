class Empleado:
    def __init__(self, nombre, puesto, salario, ide,depto):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario
        self.depto = depto
        self.ide = ide

class Nodo:
    def __init__(self,empleado):
        self.empleado = empleado
        self.siguiente = None

class ListaEmpleados:
    def __init__(self):
        self.primero = None
        self.aux = []
        

    def Vacia(self):
        return self.primero == None

    def AregarEmpleado(self, nombre, puesto, salario, ide, depto):
        if self.Vacia():
            self.primero = Nodo(Empleado(nombre,puesto,salario,ide, depto))
        else:
            primero = self.primero
            while primero.siguiente != None:
                primero = primero.siguiente
            primero.siguiente = Nodo(Empleado(nombre,puesto,salario,ide, depto))

        return Nodo(Empleado(nombre,puesto,salario,ide, depto))
    
    def BuscarNombre(self, nombre):
        empleados = []
        actual = self.primero
        print('¡Empleado(s) econtrado(s)!')
        contadorDiscos = 0
        while actual.siguiente != None:               
            if actual.empleado.nombre == nombre:
                contadorDiscos += 1
                print('_________________________________________________')
                print(f'ID empleado: {actual.empleado.ide}')
                print(f'Nombre: {actual.empleado.nombre}')
                print(f'Puesto: {actual.empleado.puesto}')
                print(f'Salario: {actual.empleado.salario}')
                print(f'Departamento: {actual.empleado.depto}')
                empleados.append(actual.empleado)
                actual = actual.siguiente             
            else:
                actual = actual.siguiente
        if actual.empleado.nombre == nombre:
            contadorDiscos += 1
            #print(f'Cantidad de discos encontrados: {self.contador}')
            print('_________________________________________________')
            print(f'ID empleado: {actual.empleado.ide}')
            print(f'Nombre: {actual.empleado.nombre}')
            print(f'Puesto: {actual.empleado.puesto}')
            print(f'Salario: {actual.empleado.salario}')
            print(f'Departamento: {actual.empleado.depto}')
            empleados.append(actual.empleado)
            #print('_________________________________________________')
            actual = actual.siguiente             
        else:
            actual = actual.siguiente
        print(f'Cantidad de empleados encontrados: {contadorDiscos}')
        return empleados

    def Buscardepto(self, depto):
        empleados = []
        actual = self.primero
        print('¡Empleado(s) econtrado(s)!')
        contadorDiscos = 0
        while actual.siguiente != None:               
            if actual.empleado.depto == (depto):
                contadorDiscos += 1
                print('_________________________________________________')
                print(f'ID empleado: {actual.empleado.ide}')
                print(f'Nombre: {actual.empleado.nombre}')
                print(f'Puesto: {actual.empleado.puesto}')
                print(f'Salario: {actual.empleado.salario}')
                print(f'Departamento: {actual.empleado.depto}')
                empleados.append(actual.empleado)
            actual = actual.siguiente             
        if actual.empleado.depto == (depto):
            contadorDiscos += 1
            print('_________________________________________________')
            print(f'ID empleado: {actual.empleado.ide}')
            print(f'Nombre: {actual.empleado.nombre}')
            print(f'Puesto: {actual.empleado.puesto}')
            print(f'Salario: {actual.empleado.salario}')
            print(f'Departamento: {actual.empleado.depto}')
            empleados.append(actual.empleado)
        print(f'Cantidad de empleados encontrados: {contadorDiscos}')
        return empleados

    def ObtenerDepto(self):
        departamentos = []
        actual = self.primero
        while actual.siguiente != None:
            if actual.empleado.depto in departamentos:
                pass
            else:
                departamentos.append(actual.empleado.depto)
            actual = actual.siguiente
        if actual.empleado.depto in departamentos:
            pass
        else:
            departamentos.append(actual.empleado.depto)
        return departamentos

    def imprimir(self):
        primero = self.primero
        departamentos = self.ObtenerDepto()
        for departamento in departamentos:
            primero = self.primero
            print(f'>> Departamento: {departamento}\n')
            while primero.siguiente!= None:
                if primero.empleado.depto == departamento:
                    print(f'\t > ID Empleado: {primero.empleado.ide}')
                    print(f'\t\t Nombre Empleado: {primero.empleado.nombre}')
                    print(f'\t\t Puesto Empleado: {primero.empleado.puesto}')
                    print(f'\t\t Salario Empleado: {primero.empleado.salario}')
                    print('')
                primero = primero.siguiente
            if primero.empleado.depto == departamento:
                print(f'\t > ID Empleado: {primero.empleado.ide}')
                print(f'\t\t Nombre Empleado: {primero.empleado.nombre}')
                print(f'\t\t Puesto Empleado: {primero.empleado.puesto}')
                print(f'\t\t Salario Empleado: {primero.empleado.salario}')
                print('')

    def Modificar(self, id,nombreN, puestoN,salarioN):
        actual = self.primero
        while actual != None:
            if actual.empleado.ide == id:
                actual.empleado.nombre = nombreN
                actual.empleado.puesto = puestoN
                actual.empleado.salario = salarioN
                return actual.empleado
            else:
                actual = actual.siguiente