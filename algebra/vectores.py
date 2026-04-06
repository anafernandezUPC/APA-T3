"""
Ana Fernández Tejero

Pruebas unitarias: 

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])

>>> v1 * v2
Vector([4, 10, 18])

>>> v1 @ v2
32

>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])

>>> v1 % v2
Vector([1.0, -1.0, 1.0])

"""

import doctest

class Vector:
    def __init__(self, datos):
        """
        Crea una instancia de Vector guardando los elementos en una lista interna.
        """
        self.lista = [item for item in datos]

    def __repr__(self):
        """
        Cadena de texto para la reconstrucción del objeto Vector.
        """
        return "Vector(" + repr(self.lista) + ")"

    def __len__(self):
        """
        Retorna la cantidad de dimensiones del vector.
        """
        return len(self.lista)

    def __getitem__(self, posicion):
        """
        Accede a una coordenada específica mediante su índice.
        """
        return self.lista[posicion]

    def __add__(self, sumando):
        """
        Realiza la suma vectorial término a término.
        """
        return Vector([x + y for x, y in zip(self.lista, sumando.lista)])

    def __sub__(self, sustraendo):
        """
        Calcula la diferencia entre dos vectores.
        """
        return Vector([x - y for x, y in zip(self.lista, sustraendo.lista)])

    def __mul__(self, operando):
        """
        Gestiona la multiplicación por un valor escalar o el producto de Hadamard.
        """
        if isinstance(operando, (int, float)):
            # Producto escalar por vector
            return Vector([val * operando for val in self.lista])

        if isinstance(operando, Vector):
            # Producto de Hadamard (elemento a elemento)
            return Vector([a * b for a, b in zip(self.lista, operando.lista)])

        return NotImplemented
        
    def __rmul__(self, escalar):
        """
        Permite la multiplicación cuando el escalar aparece a la izquierda.
        """
        return self.__mul__(escalar)

    def __matmul__(self, v_remoto):
        """
        Calcula el producto escalar (dot product) con el operador @.
        """
        return sum(i * j for i, j in zip(self.lista, v_remoto.lista))

    def __floordiv__(self, v_referencia):
        """
        Obtiene la proyección (componente paralela) sobre un vector dado.
        """
        # Proyección = (v1 · v2 / |v2|^2) * v2
        alfa = (self @ v_referencia) / (v_referencia @ v_referencia)
        return alfa * v_referencia

    def __mod__(self, v_referencia):
        """
        Calcula el vector residuo o componente normal (perpendicular).
        """
        # v_normal = v_total - v_paralelo
        return self - (self // v_referencia)

if __name__ == "__main__":
    # Ejecución de los test unitarios en modo verboso 
    doctest.testmod(verbose=True)