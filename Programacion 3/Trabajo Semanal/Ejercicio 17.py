class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Diccionario que relaciona los dígitos con sus letras correspondientes del teclado telefónico
        telefono = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Si la entrada está vacía, no hay combinaciones posibles
        if not digits:
            return []

        # Lista para guardar las combinaciones resultantes
        resultado = []

        # Función recursiva para construir las combinaciones
        def backtrack(combinacion, siguiente):
            # Si no quedan más dígitos por procesar, guardamos la combinación actual
            if not siguiente:
                resultado.append(combinacion)
                return
            # Recorremos cada letra correspondiente al primer dígito disponible
            for letra in telefono[siguiente[0]]:
                backtrack(combinacion + letra, siguiente[1:])

        # Iniciamos el proceso con una combinación vacía y la cadena completa
        backtrack("", digits)
        return resultado
