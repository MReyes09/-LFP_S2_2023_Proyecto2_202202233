from controller.error import Error
from controller.token import Token


class Analyst():

    def __init__(self, text):

        self.text = text
        self.f = 1
        self.c = 1
        self.tokens = []
        self.errores_Lex_List = []

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
                token, cadena, word = self.word_key(cadena)

                if token and cadena and word:

                    lex = Token(word, token, f, c)
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

                tipo_cor = ''

                if ascii == 91:

                     tipo_cor = "Corchete_A"

                else:

                    tipo_cor = "Corchete_C"

                char = Token(tipo_cor, caracter, f, c)
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
                cadena = self.find_Multi_Comment(cadena)
                c = self.c
                f = self.f
                puntero = 0

            elif caracter.isdigit() or ascii in (45, 43):

                self.f = f
                self.c = c
                self.tokens = tokens
                cadena = self.find_Number(cadena)
                puntero = 0
                c = self.c

            elif ascii == 35:

                lexema, cadena = self.find_comment(cadena[puntero:])

                if lexema and cadena:

                    c += 1
                    c += len(lexema)
                    puntero = 0

            elif ascii in (123, 125):

                tipo_L = ""

                if ascii == 123:

                    tipo_L = "LLave_A"

                else:

                    tipo_L = "Llave_C"

                char = Token(tipo_L, caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii in (40, 41):

                tipo_P = ""

                if ascii == 40:

                    tipo_P = "Parentesis_A"

                else:

                    tipo_P = "Parentesis_C"

                char = Token(tipo_P, caracter, f, c)
                tokens.append(char)
                c += 1
                cadena = cadena[1:]
                puntero = 0

            elif ascii == 59:

                char = Token("Punto_coma", caracter, f, c)
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

        # for token in self.tokens:
        #
        #     print(f"nombre = {token.nombre} token = {token.lexema}")

    def word_key(self, cadena):

        lexema = ''

        for caracter in cadena:

            ascii = ord(caracter)

            if not ((ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122)):

                word_Reserved = ["Claves", "Registros"]

                for word in word_Reserved:

                    if lexema == word:

                        return lexema, cadena[len(lexema):], word

                function_Reserved = ["imprimir", "imprimirln",
                     "conteo", "promedio", "contarsi", "datos", "sumar",
                     "max", "min", "exportarReporte"]

                for function in function_Reserved:

                    if lexema == function:

                        return lexema, cadena[len(lexema):], "word_key"

                return lexema, None, None

            else:

                lexema += caracter

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

    def find_Number(self, txt):

        lexema = ''
        state = 0

        for char in txt:

            ascii = ord(char)

            if state == 0:

                if ascii in (43, 45):

                    lexema += char
                    state = 3

                elif char.isdigit():

                    lexema += char
                    state = 4

            elif state == 3:

                if char.isdigit():

                    lexema += char
                    state = 4

                else:

                    self.c += len(lexema)
                    error = Error(lexema, self.c, self.f)
                    self.errores_Lex_List.append(error)

                    return txt[len(lexema):]

            elif state == 4:

                if char.isdigit():

                    lexema += char

                elif ascii == 46:

                    lexema += char
                    state = 8

                else:

                    self.c += len(lexema)
                    self.tokens.append(Token("int", int(lexema), self.f, self.c))
                    return txt[len(lexema):]

            elif state == 8:

                if char.isdigit():

                    lexema += char
                    state = 10

                else:

                    self.c += len(lexema)
                    error = Error(lexema, self.c, self.f)
                    self.errores_Lex_List.append(error)

                    return txt[len(lexema):]

            elif state == 10:

                if char.isdigit():

                    lexema += char

                else:

                    self.c += len(lexema)
                    self.tokens.append(Token("float", float(lexema), self.f, self.c))
                    return txt[len(lexema):]

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

                    error = Error(lexema, self.c, self.f)
                    self.errores_Lex_List.append(error)
                    return cadena[len(lexema):]

            elif estado == 9:

                if ascii == 39:

                    lexema += char
                    estado = 11
                    self.c = 1

                else:

                    error = Error(lexema, self.c, self.f)
                    self.errores_Lex_List.append(error)
                    return cadena[len(lexema):]

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

                    self.c += 1
                    lexema += char
                    estado = 12

            elif estado == 12:

                if ascii == 39:

                    lexema += char
                    estado = 13
                    self.c += 1

                else:

                    error = Error(lexema, self.c, self.f)
                    self.errores_Lex_List.append(error)
                    return cadena[len(lexema):]

            elif estado == 13:

                if ascii == 39:

                    lexema += char
                    self.c += 1
                    # self.tokens.append(Token("Multi_Comment", lexema, inicio[1], inicio[0]))
                    return cadena[len(lexema):]

                else:

                    error = Error(lexema, self.c, self.f)
                    self.errores_Lex_List.append(error)
                    return cadena[len(lexema):]
