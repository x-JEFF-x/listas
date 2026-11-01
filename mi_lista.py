from pasajero import Pasajero


class MiLista:
    """Lista construida a mano sobre un arreglo de tamaño fijo.
    datos     -> [p1, p2, p3, None, None, ...]
    capacidad -> total de cajones     cantidad -> cajones ocupados
    ⛔ Sin append, insert, pop, remove, sort, reverse, copy, len, in, slicing.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def añadir(self, pasajero):                      # ✅ resuelto + mejora
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        if self.buscar(pasajero.numero) != -1:        # mejora: números únicos
            print("  ⚠ Ya existe un pasajero con ese número")
            return False
        self.datos[self.cantidad] = pasajero          # primer cajón libre
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ resuelto
        if self.cantidad == 0:
            print("  (lista vacía)")
            return
        for i in range(self.cantidad):
            print(f"  [{i}] {self.datos[i]}")

    # ---------------- ✅ IMPLEMENTADO (tabla 3.1 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        # Validaciones: posición entre 0 y cantidad, lista no llena, número no repetido
        if posicion < 0 or posicion > self.cantidad:
            print("  ⚠ Posición inválida")
            return False
        if self.cantidad == self.capacidad:
            print("  ⚠ La lista está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe un pasajero con ese número")
            return False

        # Corre a la derecha DE ATRÁS HACIA ADELANTE para no pisar datos
        i = self.cantidad
        while i > posicion:
            self.datos[i] = self.datos[i - 1]
            i = i - 1

        self.datos[posicion] = pasajero               # el hueco ya está libre
        self.cantidad = self.cantidad + 1
        return True

    def buscar(self, numero):
        # Búsqueda lineal: solo los cajones ocupados (0 a cantidad-1)
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def buscar_binaria(self, numero):
        # REQUIERE la lista ordenada de menor a mayor (usar ordenar_asc antes)
        izq = 0
        der = self.cantidad - 1
        while izq <= der:
            medio = (izq + der) // 2
            if self.datos[medio].numero == numero:
                return medio
            elif self.datos[medio].numero < numero:
                izq = medio + 1                       # descarta la mitad izquierda
            else:
                der = medio - 1                       # descarta la mitad derecha
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)                # reutiliza buscar
        if posicion == -1:
            return False
        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= self.cantidad:
            return None
        eliminado = self.datos[posicion]

        # Corre a la izquierda tapando el hueco
        for i in range(posicion, self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]

        self.datos[self.cantidad - 1] = None          # el último cajón queda vacío
        self.cantidad = self.cantidad - 1
        return eliminado

    def eliminar_por_valor(self, numero):
        posicion = self.buscar(numero)                # reutiliza buscar...
        if posicion == -1:
            return False
        self.eliminar_por_posicion(posicion)          # ...y eliminar_por_posicion
        return True

    def ordenar_asc(self):
        # Burbuja por número, de menor a mayor
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_desc(self):
        # La misma burbuja: solo cambia el símbolo de comparación (> por <)
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def reversar(self):
        # Dos punteros que se acercan intercambiando
        izq = 0
        der = self.cantidad - 1
        while izq < der:
            aux = self.datos[izq]
            self.datos[izq] = self.datos[der]
            self.datos[der] = aux
            izq = izq + 1
            der = der - 1

    def copiar(self):
        nueva = MiLista(self.capacidad)               # otra lista, con otro arreglo
        for i in range(self.cantidad):
            nueva.añadir(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad                          # no hay que recorrer nada
