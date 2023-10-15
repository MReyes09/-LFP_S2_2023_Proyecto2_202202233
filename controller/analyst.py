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

                copy = cadena
                token, cadena = self.word_key(cadena)

                if token and cadena:

                    lex = Token("word_Key", token, f, c)
                    c += len(token)
                    tokens.append(lex)
                    puntero = 0

                else:

                    error = Error(token, c, f)
                    self.errores_Lex_List.append(error)
                    cadena = copy[len(token):]
                    puntero = 0
                    c += len(token)

            elif ascii == 61:

                lex = Token("igual", caracter, f, c)
                c += 1
                tokens.append(lex)
                cadena = cadena[1:]
                puntero = 0

            elif ascii in (91, 93):

                char = Token("Corchete", caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii == 34:

                lexema, cadena = self.find_Str(cadena[puntero:])

                if lexema and cadena:

                    lex = Token("String", lexema, f, c)
                    c += 1
                    c += len(lexema) + 1
                    tokens.append(lex)
                    puntero = 0

            elif ascii == 44:

                lex = Token("Coma", caracter, f, c)
                c += 1
                tokens.append(lex)
                cadena = cadena[1:]
                puntero = 0

            elif ascii == 39:
                self.f = f
                self.c = c
                self.tokens = tokens
                # self.errores_Lex_List =
                lexema, cadena = self.find_Multi_Comment(cadena)

                if lexema and cadena:
                    lex = Token("Multiline_Comment", lexema, f, c)
                    c += self.c
                    f = self.f
                    tokens.append(lex)
                    puntero = 0

            elif caracter.isdigit() or ascii in (45, 43):

                token, cadena, numero = self.find_Number(cadena)

                if token and cadena:
                    num = Token("Numero", token, f, c)
                    tokens.append(num)
                    c += len(numero)
                    puntero = 0

            elif ascii == 35:

                lexema, cadena = self.find_comment(cadena[puntero:])

                if lexema and cadena:

                    lex = Token("Line_Comment", lexema, f, c)
                    c += 1
                    c += len(lexema)
                    tokens.append(lex)
                    puntero = 0

            elif ascii in (123, 125):

                char = Token("Llave", caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii in (40, 41):

                char = Token("Parentesis", caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii == 59:

                char = Token("Punto y coma", caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii == 10:

                cadena = cadena[1:]
                puntero = 0
                f += 1
                c = 1

            elif ascii == 32:

                cadena = cadena[1:]
                puntero = 0
                c += 1

            else:

                error = Error(caracter, c, f)
                self.errores_Lex_List.append(error)
                cadena = cadena[1:]
                puntero = 0
                c += 1

        for error in self.errores_Lex_List:

            print(f"lexema = {error.lexema} f = {error.fila} c = {error.columna}")

    def word_key(self, cadena):

        lexema = ''

        for caracter in cadena:

            ascii = ord(caracter)

            if not ((ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122)):

                word_Reserved = ["Claves", "Registros", "imprimir", "imprimirln",
                     "conteo", "promedio", "contarsi", "sumar",
                     "max", "min", "exportarReporte"]

                for word in word_Reserved:

                    if lexema == word:

                        return lexema, cadena[len(lexema):]

                return lexema, None

            else:

                lexema += caracter

        return None, None

    def find_Str(self, texto):

        lexema = ''
        clave = ''

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

    def find_comment(self, cadena):

        lexema = ''

        for char in cadena:

            ascii = ord(char)

            if ascii == 10:

                return lexema, cadena[len(lexema):]

            else:

                lexema += char

        return None, None

    def find_Multi_Comment(self, cadena):

        lexema = ''
        estado = 0
        puntero = 0

        for char in cadena:

            ascii = ord(char)

            if estado == 0:

                if ascii == 39:

                    lexema += char
                    estado = 7
                    self.c += 1

            elif estado == 7:

                if ascii == 39:

                    lexema += char
                    estado = 9
                    self.c += 1

                else:

                    print("Error lexico, se esperaba una comilla")

            elif estado == 9:

                if ascii == 39:

                    lexema += char
                    estado = 11
                    self.c = 1

                else:

                    print("Error lexico, se esperaba una comilla")

            elif estado == 11:

                if not ascii == 39:

                    if ascii == 10:

                        self.f += 1
                        self.c = 1
                    else:

                        self.c += 1
                    lexema += char
                    estado = 11

                else:

                    if ascii == 10:

                        self.f += 1
                        self.c = 0
                    else:

                        self.c += 1

                    lexema += char
                    estado = 12

            elif estado == 12:

                if ascii == 39:

                    lexema += char
                    estado = 13
                    self.c += 1

                else:

                    print("Error lexico, se esperaba una comilla")

            elif estado == 13:

                if ascii == 39:

                    lexema += char
                    self.c += 1

                    return lexema, cadena[len(lexema):]

                else:

                    print("Error lexico, se esperaba una comilla")

        return None, None