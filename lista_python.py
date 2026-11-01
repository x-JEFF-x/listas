from bisect import bisect_left
from pasajero import Pasajero


class ListaPython:
    """Las mismas operaciones usando los métodos del list de Python."""

    def __init__(self):
        self.pasajeros = []

    def añadir(self, pasajero):                      # ✅ resuelto + mejora
        if self.buscar(pasajero.numero) != -1:        # mejora: números únicos
            print("  ⚠ Ya existe un pasajero con ese número")
            return False
        self.pasajeros.append(pasajero)
        return True

    def listar(self):                                 # ✅ resuelto
        if not self.pasajeros:
            print("  (lista vacía)")
            return
        for i, p in enumerate(self.pasajeros):
            print(f"  [{i}] {p}")

    # ---------------- ✅ IMPLEMENTADO (tabla 3.2 de la guía) ----------------
    def insertar(self, posicion, pasajero):
        if posicion < 0 or posicion > len(self.pasajeros):
            print("  ⚠ Posición inválida")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  ⚠ Ya existe un pasajero con ese número")
            return False
        self.pasajeros.insert(posicion, pasajero)
        return True

    def buscar(self, numero):
        # 🧩 comprensión: posiciones donde el número coincide (como máximo una)
        posiciones = [i for i, p in enumerate(self.pasajeros) if p.numero == numero]
        return posiciones[0] if posiciones else -1

    def buscar_binaria(self, numero):
        # REQUIERE la lista ordenada de menor a mayor (usar ordenar_asc antes)
        numeros = [p.numero for p in self.pasajeros]  # 🧩 solo las claves
        i = bisect_left(numeros, numero)              # primer lugar donde cabría
        if i < len(numeros) and numeros[i] == numero:
            return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)
        if posicion == -1:
            return False
        self.pasajeros[posicion].destino = nuevo_destino
        self.pasajeros[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_posicion(self, posicion):
        if posicion < 0 or posicion >= len(self.pasajeros):
            return None
        return self.pasajeros.pop(posicion)

    def eliminar_por_valor(self, numero):
        antes = len(self.pasajeros)
        # 🧩 comprensión: me quedo con todos MENOS el que tiene ese número
        self.pasajeros = [p for p in self.pasajeros if p.numero != numero]
        return len(self.pasajeros) < antes

    def ordenar_asc(self):
        self.pasajeros.sort(key=lambda p: p.numero)

    def ordenar_desc(self):
        self.pasajeros.sort(key=lambda p: p.numero, reverse=True)

    def reversar(self):
        self.pasajeros.reverse()

    def copiar(self):
        nueva = ListaPython()
        nueva.pasajeros = self.pasajeros.copy()
        return nueva

    def longitud(self):
        return len(self.pasajeros)

    def filtrar_por_destino(self, destino):           # solo Lista 2
        destino = destino.strip().lower()
        return [p for p in self.pasajeros if p.destino.lower() == destino]

    def mayores_de_edad(self):                        # solo Lista 2
        return [p for p in self.pasajeros if p.es_mayor_de_edad()]
