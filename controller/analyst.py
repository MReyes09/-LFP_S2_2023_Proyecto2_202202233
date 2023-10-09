from controller.error import Error
from controller.token import Token


class Analyst():

    def __init__(self, text):

        self.text = text
        self.f = 1
        self.c = 1
        self.tokens = []
        self.errores_Lex_List = []
        self.errores_Sem_List = []

    def analyst_Data(self):

        f = self.f
        c = self.c
        tokens = self.tokens
        cadena = self.text
        puntero = 0

        while cadena:

            caracter = cadena[puntero]
            puntero += 1
            ascii = ord(caracter)

            if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):

                token, cadena = self.word_key(cadena)

                if token and cadena:

                    lex = Token("word_Key", token, f, c)
                    c += len(token)
                    tokens.append(lex)
                    puntero = 0

            elif ascii == 34:

                lexema, cadena = self.find_Str(cadena[puntero:])

                if lexema and cadena:
                    lex = Token("String", lexema, f, c)
                    c += 1
                    c += len(lexema) + 1
                    tokens.append(lex)
                    puntero = 0

            elif caracter.isdigit() or ascii in (45, 43):

                token, cadena, numero = self.find_Number(cadena)

                if token and cadena:
                    num = Token("Numero", token, f, c)
                    tokens.append(num)
                    c += len(numero)
                    puntero = 0

            elif ascii in (91, 93):

                char = Token("Corchete", caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii in (123, 125):

                char = Token("Llave", caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii == 9:

                c += 3
                cadena = cadena[3:]  # Se cortan los espacios de la tabulacion
                puntero = 0

            elif ascii == 10:

                cadena = cadena[1:]
                puntero = 0
                f += 1
                c = 1

            elif ascii in (32, 61, 44, 59):

                cadena = cadena[1:]
                puntero = 0
                c += 1

            else:

                cadena = cadena[1:]
                puntero = 0
                c += 1

        for token in tokens:

            print(f"nombre: {token.nombre} - lexema: {token.lexema} - fila: {token.fila} - columna: {token.columna}")

    def word_key(self, cadena):

        lexema = ''

        for caracter in cadena:

            ascii = ord(caracter)

            if not ((ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122)):

                return lexema, cadena[len(lexema):]

            else:

                lexema += caracter
        return None, None

    def find_Str(self, texto):

        lexema = ''
        clave = ''
        # "HOLA"
        for caracter in texto:

            ascii = ord(caracter)
            clave += caracter

            if ascii == 34:  # CARACTER = "

                return lexema, texto[len(clave):]

            else:

                lexema += caracter

        return None, None

    def find_Number(self, texto):

        numero = ''
        clave = ''
        verificar = False

        for caracter in texto:

            clave += caracter
            ascii = ord(caracter)

            if ascii == 46:
                verificar = True

            if ascii in (46, 45) or caracter.isdigit():

                numero += caracter

            else:

                if verificar:

                    return float(numero), texto[len(clave) - 1:], numero

                else:

                    return int(numero), texto[len(clave) - 1:], numero

        return None, None, None
