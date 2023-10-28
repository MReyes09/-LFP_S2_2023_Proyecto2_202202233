from controller.error import Error
from controller.results import Results
from controller.token import Token

class Sintactico():
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.listaClaves = []
        self.listaRegistros = []
        self.errores_Sintacticos = []
        self.results = []

        #Controlar que se llegó al final de la lista de tokens
        tokenNuevo = Token('EOF', 'EOF', 0, 0)
        self.tokens.append(tokenNuevo)

    def analyst_Syntactic(self):

        self.inicio()

    def inicio(self):

        self.claves()
        self.registros()
        self.funciones()
        print(self.listaClaves)
        print(self.listaRegistros)

    # <Claves> ::= Claves igual Corchete_A String <otra_Clave> Corchete_C
    def claves(self):

        if self.tokens[0].nombre == "Claves":

            self.tokens.pop(0)

            if self.tokens[0].nombre == "igual":

                self.tokens.pop(0)

                if self.tokens[0].nombre == "Corchete_A":

                    self.tokens.pop(0)

                    if self.tokens[0].nombre == "String":

                        clave = self.tokens.pop(0)
                        self.listaClaves.append(clave.lexema)
                        self.otraClave()

                        if self.tokens[0].nombre == "Corchete_C":

                            self.tokens.pop(0)

                        else:

                            descripcion = f"Se esperaba ] se obtuvo {self.tokens[0].nombre}"
                            self.agregar_Error(self.tokens[0], descripcion)
                            self.recuperarDos("Registros", "word_key")

                    else:

                        descripcion = f"Se esperaba String se obtuvo {self.tokens[0].nombre}"
                        self.agregar_Error(self.tokens[0], descripcion)
                        self.recuperar("Corchete_C")

                else:

                    descripcion = f"Se esperaba [ se obtuvo {self.tokens[0].nombre}"
                    self.agregar_Error(self.tokens[0], descripcion)
                    self.recuperar("Corchete_C")

            else:

                descripcion = f"Se esperaba = se obtuvo {self.tokens[0].nombre}"
                self.agregar_Error(self.tokens[0], descripcion)
                self.recuperar("Corchete_C")

        else:

            descripcion = f"Se esperaba Clavaes se obtuvo {self.tokens[0].nombre}"
            self.agregar_Error(self.tokens[0], descripcion)
            self.recuperar("Corchete_C")

    def agregar_Error(self, token, descripcion):

        lexema = descripcion
        fila = token.fila
        columna = token.columna
        error = Error(lexema, columna, fila)
        error.tipo = "Sintactico"
        self.errores_Sintacticos.append(error)

    #<otra_Clave> ::= coma String <otra_Clave>
    def otraClave(self):

        if self.tokens[0].nombre == "Coma":

            self.tokens.pop(0)

            if self.tokens[0].nombre == "String":

                clave = self.tokens.pop(0)
                self.listaClaves.append(clave.lexema)
                self.otraClave()

            else:

                descripcion = f"Se esperaba String se obtuvo {self.tokens[0].nombre}"
                self.agregar_Error(self.tokens[0], descripcion)
                self.recuperarDos("Corchete_C", "Registros")

    # ------------------------------------------------

    # <Registros> ::= Registros igual Corchete_A <Registro> <otro_Registro> Corchete_C
    def registros(self):

        if self.tokens[0].nombre == "Registros":

            self.tokens.pop(0)

            if self.tokens[0].nombre == "igual":

                self.tokens.pop(0)

                if self.tokens[0].nombre == "Corchete_A":

                    self.tokens.pop(0)
                    self.registro()
                    self.otroRegistro()

                    if self.tokens[0].nombre == "Corchete_C":

                        self.tokens.pop(0)

                    else:

                        descripcion = f"Se esperaba ] se obtuvo {self.tokens[0].nombre}"
                        self.agregar_Error(self.tokens[0], descripcion)
                        self.recuperar("word_key")

                else:

                    descripcion = f"Se esperaba [ se obtuvo {self.tokens[0].nombre}"
                    self.agregar_Error(self.tokens[0], descripcion)
                    self.recuperarDos("Corchete_C", "word_key")

            else:

                descripcion = f"Se esperaba = se obtuvo {self.tokens[0].nombre}"
                self.agregar_Error(self.tokens[0], descripcion)
                self.recuperarDos("Corchete_C", "word_key")

        else:

            descripcion = f"Se esperaba Registros se obtuvo {self.tokens[0].nombre}"
            self.agregar_Error(self.tokens[0], descripcion)
            self.recuperarDos("Registros", "word_key")

    #<Registro> ::= LLave_A <Valor> <otro_Valor> Llave_C
    def registro(self):

        if self.tokens[0].nombre == "LLave_A":

            self.tokens.pop(0)
            res = self.valor()

            if res is not None:

                registro = []
                registro.append(res.lexema)
                self.otroValor(registro)

                if self.tokens[0].nombre == "Llave_C":

                    self.tokens.pop(0)
                    self.listaRegistros.append(registro)

                else:

                    descripcion = ("Se esperaba } se obtuvo ", self.tokens[0].nombre)
                    self.agregar_Error(self.tokens[0], descripcion)
                    self.recuperarDos("Corchete_C", "word_key")

        else:

            descripcion = ("Se esperaba { se obtuvo ", self.tokens[0].nombre)
            self.agregar_Error(self.tokens[0], descripcion)
            self.recuperar("word_key")

    # <Valor> ::= String
    #             | int
    #             | float
    def valor(self):

        if self.tokens[0].nombre in ("String", "int", "float"):

            campo = self.tokens.pop(0)
            return campo

        else:

            descripcion = f"Se esperaba un valor se obtuvo {self.tokens[0].nombre}"
            self.agregar_Error(self.tokens[0], descripcion)
            self.recuperarDos("coma", "word_key")


    # <otro_Valor> ::= coma <Valor> <otro_Valor>
    def otroValor(self, registro):

        if self.tokens[0].nombre == "Coma":

            self.tokens.pop(0)
            res = self.valor()

            if res is not None:

                registro.append(res.lexema)
                self.otroValor(registro)

    # <otro_Registro> ::= <Registro><otro_Registro>
    #                         | ε
    def otroRegistro(self):

        if self.tokens[0].nombre == "LLave_A":

            self.registro()
            self.otroRegistro()

    #<Funciones> ::= <Funcion> <otra_Funcion>
    def funciones(self):
        self.funcion()
        self.otraFuncion()

    # <funcion> ::= word_key Parentesis_A <Parametros> Parentesis_C Punto_coma

    def funcion(self):
        if self.tokens[0].nombre == 'word_key':
            tipo = self.tokens.pop(0)
            if self.tokens[0].nombre == 'Parentesis_A':
                self.tokens.pop(0)
                parametros = self.parametros()
                if self.tokens[0].nombre == "word_key":
                    return
                if self.tokens[0].nombre == 'Parentesis_C':
                    self.tokens.pop(0)
                    if self.tokens[0].nombre == 'Punto_coma':
                        self.tokens.pop(0)
                        self.operarFuncion(tipo, parametros)
                    else:
                        descripcion = f"Se esperaba ; se obtuvo {self.tokens[0].nombre}"
                        self.agregar_Error(self.tokens[0], descripcion)
                        self.recuperar("word_key")
                else:
                    descripcion = f"Se esperaba ) se obtuvo {self.tokens[0].nombre}"
                    self.agregar_Error(self.tokens[0], descripcion)
                    self.recuperar("word_key")

            else:
                descripcion = f"Se esperaba ( se obtuvo {self.tokens[0].nombre}"
                self.agregar_Error(self.tokens[0], descripcion)
                self.recuperar("word_key")
        else:
            descripcion = f"Se esperaba word_Key se obtuvo {self.tokens[0].nombre}"
            self.agregar_Error(self.tokens[0], descripcion)
            self.recuperar("word_key")

        # <parametros> ::= <valor> <otroParametro>
        #               | ε

    def parametros(self):
        parametros = []
        if self.tokens[0].nombre != 'Parentesis_C':
            valor = self.valor()
            if valor is not None:
                parametros = [valor]
                self.otroParametro(parametros)
        return parametros

        # <otroParametro> ::= coma <Valor> <otro_Parametro>
        #                  | ε

    def otroParametro(self, parametros):
        if self.tokens[0].nombre == 'Coma':
            self.tokens.pop(0)
            valor = self.valor()
            if valor is not None:
                parametros.append(valor)
                self.otroParametro(parametros)

        # <otraFuncion> ::= <funcion> <otraFuncion>
        #                | ε

    def otraFuncion(self):
        if self.tokens[0].nombre != 'EOF':
            self.funcion()
            self.otraFuncion()
        else:
            print("Análisis terminado")

        # Operación de funciones

    def operarFuncion(self, tipo, parametros):

        if len(self.errores_Sintacticos) != 0:
            return

        if tipo.lexema == 'imprimir':

            if len(parametros) == 1:

                resultado = Results(tipo.lexema, parametros[0].lexema)

                if len(self.results) == 0:

                    self.results.append(resultado)

                else:

                    if self.results[-1].f == "imprimir":

                        self.results[-1].r += parametros[0].lexema

                    else:

                        self.results.append(resultado)
            else:

                error = Error(f"Se esperaba 1 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'imprimirln':

            if len(parametros) == 1:

                resultado = Results(tipo.lexema, parametros[0].lexema)
                self.results.append(resultado)

            else:

                error = Error(f"Se esperaba 1 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'conteo':
            if len(parametros) == 0:

                resultado = Results(tipo.lexema, len(self.listaRegistros))
                self.results.append(resultado)

            else:

                error = Error(f"Se esperaba 0 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'promedio':

            if len(parametros) == 1:

                if parametros[0].nombre == 'String':

                    res = self.promedio(parametros[0].lexema)
                    if res is None:

                        resultado = Results(tipo.lexema, f"No se encontro {parametros[0].lexema}")
                        self.results.append(resultado)

                    else:

                        resultado = Results(tipo.lexema, res)
                        self.results.append(resultado)

                else:

                    error = Error(f"Se esperaba un String", tipo.columna, tipo.fila)
                    error.tipo = "Sintactico"
                    self.errores_Sintacticos.append(error)
            else:

                error = Error(f"Se esperaba 1 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'contarsi':
            if len(parametros) == 2:
                if parametros[0].nombre == 'String' and parametros[1].nombre == "int":

                    dato = self.contarsi(parametros[0].lexema, parametros[1].lexema)
                    if dato is None:
                        dato = 0
                    resultado = Results(tipo.lexema, dato)
                    self.results.append(resultado)

                else:
                    error = Error(f"Los valores no son los que se esperaban", tipo.columna, tipo.fila)
                    error.tipo = "Sintactico"
                    self.errores_Sintacticos.append(error)
            else:
                error = Error(f"Se esperaba 2 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == "datos":

            if len(parametros) == 0:

                res = "CODIGO   PRODUCTO   PRECIO COMPRA   PRECIO VENTA   STOCK\n"

                for registros in self.listaRegistros:

                    fila = "  "
                    vuelta = 0

                    for dato in registros:

                        vuelta += 1
                        if vuelta == 1:

                            fila += f"{dato}      "

                        else:

                            fila += f"{dato}         "

                    res += f"{fila}\n"

                resultado = Results(tipo.lexema, res)
                self.results.append(resultado)

            else:

                error = Error(f"Se esperaba 0 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'sumar':

            if len(parametros) == 1:

                if parametros[0].nombre == 'String':

                    res = self.sumar_Datos(parametros[0].lexema)

                    if res is None:

                        error = Error(f"El campo dado {parametros[0].lexema} posee datos String, no se puede sumar", tipo.columna, tipo.fila)
                        error.tipo = "Sintactico"
                        self.errores_Sintacticos.append(error)

                    else:

                        resultado = Results(tipo.lexema, res)
                        self.results.append(resultado)

                else:

                    error = Error(f"Se esperaba un String", tipo.columna, tipo.fila)
                    error.tipo = "Sintactico"
                    self.errores_Sintacticos.append(error)

            else:

                error = Error(f"Se esperaba 1 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'max':
            if len(parametros) == 1:
                if parametros[0].nombre == 'String':

                    res = self.max_min_Data(parametros[0].lexema, 1)

                    if res is None:

                        error = Error(f"El campo dado {parametros[0].lexema} posee datos String, no se puede sumar", tipo.columna, tipo.fila)
                        error.tipo = "Sintactico"
                        self.errores_Sintacticos.append(error)

                    else:

                        resultado = Results(tipo.lexema, res)
                        self.results.append(resultado)

                else:
                    error = Error(f"Se esperaba un String", tipo.columna, tipo.fila)
                    error.tipo = "Sintactico"
                    self.errores_Sintacticos.append(error)
            else:
                error = Error(f"Se esperaba 1 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'min':
            if len(parametros) == 1:
                if parametros[0].nombre == 'String':
                    res = self.max_min_Data(parametros[0].lexema, 2)

                    if res is None:

                        error = Error(f"El campo dado {parametros[0].lexema} posee datos String, no se puede sumar", tipo.columna, tipo.fila)
                        error.tipo = "Sintactico"
                        self.errores_Sintacticos.append(error)

                    else:

                        resultado = Results(tipo.lexema, res)
                        self.results.append(resultado)
                else:
                    error = Error(f"Se esperaba un String", tipo.columna, tipo.fila)
                    error.tipo = "Sintactico"
                    self.errores_Sintacticos.append(error)
            else:
                error = Error(f"Se esperaba 1 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        elif tipo.lexema == 'exportarReporte':
            if len(parametros) == 1:
                if parametros[0].nombre == 'String':
                    self.generar_reporte_html(parametros[0].lexema)
                    resultado = Results(tipo.lexema, None)
                    self.results.append(resultado)
                else:
                    error = Error(f"Se esperaba un String", tipo.columna, tipo.fila)
                    error.tipo = "Sintactico"
                    self.errores_Sintacticos.append(error)
            else:
                error = Error(f"Se esperaba 1 parametro, se recibieron {len(parametros)}", tipo.columna, tipo.fila)
                error.tipo = "Sintactico"
                self.errores_Sintacticos.append(error)

        # Producción <promedio> -> tk_promedio <CadenaFin>

    def generar_reporte_html(self, titulo):

        try:
            with open(f"{titulo}.html", "w", encoding="utf-8") as archivo:
                # Encabezado del documento HTML con meta UTF-8 y estilo CSS de W3Schools
                archivo.write(f"""<!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
        </head>
        <body>
            <h1>{titulo}</h1>
            <table class="w3-table w3-striped">
                <tr>
                    <th>código</th>
                    <th>producto</th>
                    <th>precio_compra</th>
                    <th>precio_venta</th>
                    <th>stock</th>
                </tr>
        """)

                # Agregar filas de datos a la tabla
                for dato in self.listaRegistros:
                    fila = "\t\t<tr>\n"
                    for elemento in dato:
                        fila += f"\t\t\t<td>{elemento}</td>\n"
                    fila += "\t\t</tr>\n"
                    archivo.write(fila)

                # Cierre del documento HTML
                archivo.write("""    </table>
        </body>
        </html>""")

        except Exception as e:

            print(e)

    def max_min_Data(self, campo, tipo):

        encontrado = False
        posicion = -1
        for c in self.listaClaves:
            posicion += 1
            if c == campo and c != "producto":
                encontrado = True
                break
        if encontrado:
            lista = []
            for registro in self.listaRegistros:
                lista.append(registro[posicion])

            if tipo == 1:
                return max(lista)
            elif tipo == 2:
                return min(lista)
        return None

    def sumar_Datos(self, campo):

        encontrado = False
        posicion = -1
        for c in self.listaClaves:
            posicion += 1
            if c == campo and c != "producto":
                encontrado = True
                break
        if encontrado:
            suma = 0

            for registro in self.listaRegistros:
                if isinstance(registro[posicion], str):
                    suma += len(registro[posicion])
                else:
                    suma += registro[posicion]
            return suma
        return None

    def contarsi(self, campo1, campo2):

        encontrado = False
        posicion = -1

        for c in self.listaClaves:

            posicion += 1

            if c == campo1:

                encontrado = True
                break

        if encontrado:

            encontrado2 = False

            for registro in self.listaRegistros:

                for dato in registro:

                    if dato == campo2:

                        encontrado2 = True
                        break

                if encontrado2 is True:

                    return registro[posicion]

            return None

        else:

            return None

    def promedio(self, campo):
        encontrado = False
        posicion = -1
        for c in self.listaClaves:
            posicion += 1
            if c == campo:
                encontrado = True
                break
        if encontrado:
            suma = 0
            promedio = 0
            for registro in self.listaRegistros:
                if isinstance(registro[posicion], str):
                    suma += len(registro[posicion])
                else:
                    suma += registro[posicion]
            if len(self.listaRegistros) > 0:
                promedio = suma / len(self.listaRegistros)
            return promedio
        return None

    def recuperar(self, nombreToken):
        while self.tokens[0].nombre != 'EOF':
            if self.tokens[0].nombre == nombreToken:
                if self.tokens[0].nombre in ("Registros", "Claves", "word_key"):
                    return
                self.tokens.pop(0)
            else:
                self.tokens.pop(0)

    def recuperarDos(self, nombreToken1, nombreToken2):
        while self.tokens[0].nombre != 'EOF':
            if self.tokens[0].nombre in (nombreToken1, nombreToken2):
                if self.tokens[0].nombre in ("Registros", "Claves", "word_key", "coma"):
                    return
                self.tokens.pop(0)
            else:
                self.tokens.pop(0)
