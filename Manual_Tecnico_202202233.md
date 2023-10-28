#####  Universidad de San Carlos de Guatemala
#####  Facultad de Ingeniería
#####  Escuela de Ciencias y Sistemas
#####  Laboratorio de Lenguajes Formales y de Programación
##### **Matthew Emmanuel Reyes Melgar 202202233**

# Manual Técnico

## Descripción General:

BizData es una plataforma diseñada para permitir a las pequeñas empresas tomar decisiones estratégicas fundamentadas basadas en el análisis profundo de sus datos comerciales. Este software proporciona capacidades para cargar, analizar y generar reportes a partir de archivos estructurados en un formato especializado con extensión ".bizdata".

# Clase `Analyst` - Analizador Léxico

La clase `Analyst` implementa un analizador léxico en Python. Su principal función es analizar un texto fuente para identificar y dividir en tokens los componentes léxicos.

## Métodos Principales

### `__init__(self, text)`
Constructor de la clase, recibe el texto a analizar.

### `analyst_Data(self)`
Método principal para el análisis del texto. Divide el texto en tokens como palabras clave, identificadores, números, caracteres especiales y comentarios.

### `word_key(self, cadena)`
Identifica si una palabra en el texto es una palabra clave reservada o un identificador.

### `find_Str(self, texto)`
Busca y devuelve una cadena encerrada entre comillas dobles (" ").

### `find_Number(self, txt)`
Identifica y devuelve números enteros o flotantes del texto.

### `find_comment(self, cadena)`
Busca comentarios de una sola línea.

### `find_Multi_Comment(self, cadena)`
Busca comentarios de múltiples líneas.

## Atributos Principales

- `text`: Texto a analizar.
- `f` y `c`: Variables de fila y columna para rastrear la posición actual en el texto.
- `tokens`: Almacena los tokens identificados durante el análisis.
- `errores_Lex_List`: Registra los errores léxicos encontrados durante el análisis.

## Funcionalidades Clave

- **Identificación de Tokens:** Clasifica palabras clave reservadas, identificadores, números, caracteres especiales y comentarios.
- **Manejo de Errores:** Registra errores léxicos encontrados durante el análisis.

El análisis léxico es un paso crucial en la traducción del código fuente. Esta clase podría formar parte de un sistema más grande, como un compilador o un intérprete.


## Clase Sintactico

La clase `Sintactico` se encarga del análisis sintáctico de tokens para la plataforma BizData, la cual utiliza para interpretar las estructuras de datos definidas en un formato específico ".bizdata".

### Métodos

#### `__init__(self, tokens)`

- **Descripción:** Es el constructor de la clase `Sintactico`. Inicializa las variables y agrega un token de finalización a la lista de tokens.
- **Parámetros:**
  - `tokens`: Lista de tokens que se analizarán.

#### `analyst_Syntactic(self)`

- **Descripción:** Método principal que inicia el análisis sintáctico llamando a la función `inicio()`.

#### `inicio(self)`

- **Descripción:** Inicia el análisis, llamando a las funciones `claves()`, `registros()`, y `funciones()`, e imprime las listas de claves y registros.

#### `agregar_Error(self, token, descripcion)`

- **Descripción:** Agrega un error sintáctico a la lista de errores.
- **Parámetros:**
  - `token`: Token que ha causado el error.
  - `descripcion`: Descripción del error.

#### `claves(self)`

- **Descripción:** Analiza la producción para las claves en el código, validando su estructura y generando errores si es necesario.

#### `otraClave(self)`

- **Descripción:** Análisis de claves adicionales siguiendo una estructura específica.

#### `registros(self)`

- **Descripción:** Analiza la producción para los registros en el código, validando su estructura y generando errores si es necesario.

#### `registro(self)`

- **Descripción:** Analiza un registro específico y sus valores asociados en el código, verificando su estructura y generando errores si es necesario.

#### `valor(self)`

- **Descripción:** Analiza el valor asociado a un registro, validando su estructura.

#### `otroValor(self, registro)`

- **Descripción:** Analiza otros valores asociados a un registro en la estructura dada.

#### `otroRegistro(self)`

- **Descripción:** Analiza otros registros en la estructura, en caso de existir.

#### `funciones(self)`

- **Descripción:** Analiza la presencia de funciones en el código y llama a la función `funcion()` y `otraFuncion()`.

#### `funcion(self)`

- **Descripción:** Analiza una función específica en el código y verifica su estructura.

#### Otros métodos (como `parametros`, `otroParametro`, `otraFuncion`, `operarFuncion`, entre otros) tienen una función específica en el análisis sintáctico, validando estructuras y generando errores según sea necesario.

### Consideraciones Finales

La clase `Sintactico` es esencial para el análisis de la estructura de datos definida en un formato ".bizdata". Sus métodos verifican la sintaxis del código según las reglas establecidas y generan una lista de errores sintácticos cuando se identifican problemas, proporcionando información valiosa para la corrección y depuración del código.
