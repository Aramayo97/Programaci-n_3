class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Si x es 0 o 1, la raíz cuadrada entera es el mismo número
        if x < 2:
            return x

        # Definimos los límites para la búsqueda binaria
        izquierda, derecha = 1, x // 2

        # Búsqueda binaria
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2

            # Si encontramos el cuadrado exacto, lo devolvemos
            if medio * medio == x:
                return medio

            # Si el cuadrado de medio es menor que x, buscamos a la derecha
            if medio * medio < x:
                izquierda = medio + 1
            else:
                # Si el cuadrado de medio es mayor que x, buscamos a la izquierda
                derecha = medio - 1

        # Cuando termina el bucle, derecha es el entero más cercano hacia abajo
        return derecha
