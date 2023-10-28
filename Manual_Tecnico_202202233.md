#####  Universidad de San Carlos de Guatemala
#####  Facultad de Ingeniería
#####  Escuela de Ciencias y Sistemas
#####  Laboratorio de Lenguajes Formales y de Programación
##### **Matthew Emmanuel Reyes Melgar 202202233**

# Manual Técnico

## Descripción General

El presente manual técnico proporciona información detallada sobre el desarrollo y funcionamiento del proyecto No. 1, una aplicación numérica con análisis léxico. El objetivo principal de este proyecto es permitir a los estudiantes crear una herramienta capaz de reconocer un lenguaje dado mediante un analizador léxico que cumpla con las reglas establecidas, además de manejar la lectura y escritura de archivos para el procesamiento de información. Todo esto se logra a través de una interfaz gráfica.

## Objetivos

### Objetivo General

El objetivo general de este proyecto es que el estudiante desarrolle una aplicación que implemente un analizador léxico para reconocer un lenguaje específico a partir de código fuente en formato JSON, gestionando la detección de errores léxicos y la ejecución de instrucciones.

### Objetivos Específicos

- Implementar un analizador léxico basado en estados.
- Utilizar funciones de manejo de cadenas de caracteres en Python.
- Programar un Scanner para el análisis léxico.
- Construir un scanner basado en un autómata finito determinístico.
- Crear una interfaz gráfica interactiva utilizando Tkinter.
- Generar diagramas de operaciones con la librería Graphviz.

## Descripción Funcional

La aplicación se desarrolla en Python y utiliza la librería Tkinter para la interfaz de usuario. Su funcionalidad principal incluye:

- Lectura y edición de código fuente en formato JSON.
- Identificación de instrucciones y ejecución de las mismas.
- Generación de representaciones gráficas de árboles de operaciones.
- Detección y registro de errores léxicos en un archivo JSON.

## Interfaz de Usuario

### Menú

- **Archivo**:
  - Abrir: Permite abrir un archivo existente.
  - Guardar: Guarda el archivo actual con el mismo nombre.
  - Guardar como: Permite guardar el archivo con un nombre diferente.
  - Salir: Cierra la aplicación.

- **Analizar**: Analiza el texto y muestra los elementos reconocidos.

- **Errores**: Muestra los errores detectados en el último archivo compilado.

- **Reporte**: Genera diagramas de las operaciones analizadas.

## Operaciones Válidas

La aplicación reconoce las siguientes operaciones:

- SUMA: Suma de 2 o más números u operaciones anidadas.
- RESTA: Resta de 2 o más números u operaciones anidadas.
- MULTIPLICACIÓN: Multiplicación de 2 o más números u operaciones anidadas.
- DIVISIÓN: División entre números u operaciones anidadas.
- POTENCIA: Potencia N de un número u operación anidada.
- RAIZ: Raíz N de un número u operación anidada.
- INVERSO: Inverso de un número u operación anidada.
- SENO: Función trigonométrica seno de un número u operación anidada.
- COSENO: Función trigonométrica coseno de un número u operación anidada.
- TANGENTE: Función trigonométrica tangente de un número u operación anidada.
- MOD: Residuo entre números u operaciones anidadas.

Este manual técnico proporciona una guía completa para comprender y utilizar el proyecto No. 1, incluyendo detalles sobre su diseño, funcionalidades, interfaz de usuario y operaciones reconocidas.

## Código Fuente - Clase Ventana Principal

### **Clase `Ventana_Principal`**

La clase `Ventana_Principal` representa la ventana principal de la aplicación y contiene todos los elementos de la interfaz gráfica. Aquí se describen los principales atributos y métodos de esta clase:

- **Constructor (`__init__`):** En el constructor, se inicializan los atributos y se configuran los widgets de la interfaz gráfica, como botones, cuadros de texto y el ComboBox. Además, se establece el título de la ventana y se define su tamaño.

- **`mostrar_Componentes()`:** Este método se encarga de mostrar los componentes de la ventana en la interfaz gráfica. Configura el ComboBox y los botones en la barra de navegación, y coloca los cuadros de texto para la entrada de código y la numeración de líneas.

- **Funcionalidad de Numeración de Líneas:** Se activa la funcionalidad de numeración de líneas en el cuadro de texto `txtArea` para mantener la numeración sincronizada con el contenido del cuadro de texto. Se utilizan eventos como la liberación de teclas (`"<KeyRelease>"`) y el desplazamiento de la rueda del ratón (`"<MouseWheel>"`).

- **Funcionalidad del ComboBox (`cmb`):** Se vincula la función `accion_cmb` al evento de selección de elementos del ComboBox. Esta función se encarga de realizar acciones específicas según la opción seleccionada en el ComboBox, como abrir un archivo o guardar el contenido.

- **Funcionalidad del Botón "Analizar":** Se vincula la función `analizador_Lex` al evento de hacer clic en el botón "Analizar". Esta función inicia el análisis léxico del código ingresado por el usuario.

- **Variable `scanner`:** Se inicializa la variable `self.scanner` como `None`, que se utilizará en el análisis léxico.

- **Funcionalidad del Botón "Errores":** Se vincula la función `generar_JSON_Errores` al evento de hacer clic en el botón "Errores". Esta función genera un archivo JSON que contiene los errores encontrados durante el análisis léxico.

#### -- Función Guardar Como 
La función `guardar_Como` tiene como propósito permitir al usuario guardar el contenido del cuadro de texto (`txtArea`) en un archivo JSON con una ubicación y nombre de archivo específicos, seleccionados por el usuario a través de un cuadro de diálogo. Aquí están los pasos clave de su funcionamiento:

1.  **Solicitud de Ruta y Nombre de Archivo**: La función utiliza `filedialog.asksaveasfilename` para mostrar un cuadro de diálogo que permite al usuario seleccionar una ubicación y proporcionar un nombre de archivo para guardar.
    
2.  **Validación de Selección**: Verifica si el usuario seleccionó una ubicación y proporcionó un nombre de archivo válido. Si es así, la ruta completa se almacena en la variable `file_path`.
    
3.  **Actualización de la Ruta**: La variable `self.file_path` se actualiza con la nueva ubicación seleccionada por el usuario.
    
4.  **Obtención del Contenido**: El contenido actual del cuadro de texto (`txtArea`) se obtiene utilizando el método `self.txtArea.get(1.0, tk.END)`.
    
5.  **Escritura en el Archivo**: Se abre el archivo seleccionado en modo escritura (`'w'`) y se escribe el contenido del cuadro de texto en el archivo.
    
6.  **Confirmación de Éxito**: Si la operación de escritura se realiza con éxito, se muestra un mensaje informativo que indica que el archivo se ha guardado satisfactoriamente en la ubicación seleccionada.
    
7.  **Manejo de Errores**: Si se produce algún error durante el proceso, se captura la excepción y se muestra un mensaje de error indicando que se ha producido un problema al intentar guardar el archivo.

#### --Funcion generar_JSON_Errores

Esta función se encarga de generar un archivo JSON que contiene información sobre los errores detectados durante el análisis léxico. A continuación, se describe su funcionamiento de manera general:

-   **Obtención del Analizador Léxico (`scan`):** La función obtiene una instancia del analizador léxico almacenado en `self.scanner`, que es una instancia de la clase `Analizador`.
    
-   **Verificación de la Existencia del Analizador:** Se verifica si existe un analizador (`scan`). Si no existe, se muestra un mensaje de advertencia indicando que se debe analizar el texto antes de utilizar esta función.
    
-   **Generación del JSON de Errores:** Si se encuentra un analizador válido, la función procede a crear un archivo JSON que contiene información sobre los errores léxicos encontrados durante el análisis. Cada error se almacena en una estructura de datos JSON que incluye detalles como el lexema, el tipo de error, la columna y la fila donde se produjo.
    
-   **Escritura en el Archivo JSON:** Los datos de los errores se escriben en el archivo JSON, que se crea en el directorio de trabajo actual con el nombre "Errores_202202233.json". La función `json.dump` se utiliza para formatear y escribir los datos en el archivo con un formato legible.
    
-   **Mensajes de Información y Error:** Se muestra un mensaje de información si el archivo JSON se ha creado correctamente. En caso de que ocurra algún error durante el proceso de creación del archivo, se muestra un mensaje de error junto con detalles adicionales sobre el error.

## Código Fuente Clase Analizador

La clase `Analizador` que has proporcionado parece ser una clase que se utiliza para realizar análisis léxicos en un texto dado. A continuación, se explican los atributos y el constructor de la clase:

-   **`texto`**: Este atributo almacena el texto que se va a analizar léxicamente. El texto es el que se pasa como argumento al constructor al crear una instancia de la clase.
    
-   **`f` y `c`**: Estos atributos, `f` (fila) y `c` (columna), parecen utilizarse para rastrear la posición actual dentro del texto durante el análisis. Inicialmente, `f` se establece en 1 (posición de fila) y `c` se establece en 1 (posición de columna).
    
-   **`tokens`**: Este atributo es una lista vacía que se utiliza para almacenar los tokens que se encuentran durante el análisis léxico. Los tokens son unidades léxicas, como palabras clave, identificadores, números, etc., que se extraen del texto.
    
-   **`errores_List`**: Este atributo es una lista vacía que se utiliza para almacenar los errores léxicos que se detectan durante el análisis. Los errores léxicos son problemas en el texto que violan las reglas de la gramática del lenguaje.
    
-   **`accion`**: No se proporciona información sobre cómo se utiliza este atributo en el fragmento de código que has compartido, por lo que su funcionalidad específica no está clara.

### - Funcion Analizar

  
Se utiliza para realizar el análisis léxico del texto almacenado en el atributo `texto` de dicha clase. El análisis léxico implica dividir el texto en unidades léxicas llamadas tokens, y aquí se describe de manera general cómo esta función realiza ese proceso:

1.  Se inicializan variables como `f`, `c`, `tokens`, `cadena`, y `puntero` que se utilizarán durante el análisis:
    
    -   `f` y `c` representan la fila y columna actuales dentro del texto.
    -   `tokens` es una lista que almacenará los tokens encontrados.
    -   `cadena` contiene el texto a analizar.
    -   `puntero` se utiliza para rastrear la posición actual en `cadena`.
2.  Se inicia un bucle `while` que continuará hasta que `cadena` esté vacía, lo que significa que se ha analizado todo el texto.
    
3.  Se extrae el primer carácter de `cadena` y se almacena en la variable `caracter`. Luego, se incrementa `puntero` en 1 para avanzar al siguiente carácter.
    
4.  Se verifica el valor ASCII del carácter `caracter` para determinar qué tipo de token se encuentra.
    
5.  Dependiendo del tipo de carácter encontrado, se realizan acciones específicas:
    
    -   Si el carácter es una comilla doble (ASCII 34), se busca una cadena delimitada por comillas dobles (`" "`) y se crea un token de tipo `Lexema` para representar la cadena.
    -   Si el carácter es un dígito o un signo negativo (ASCII 45), se busca un número y se crea un token de tipo `Numero`.
    -   Si el carácter es `[` o `]` (ASCII 91 o 93), se crea un token de tipo `Lexema` para representar el carácter.
    -   Si el carácter es una tabulación (ASCII 9), se ajusta la columna `c` y se cortan los espacios de la tabulación.
    -   Si el carácter es un salto de línea (ASCII 10), se ajusta la fila `f`, la columna `c` y se elimina el salto de línea.
    -   Si el carácter es un espacio en blanco (ASCII 32), se elimina el espacio en blanco.
6.  Si el carácter no coincide con ninguno de los casos anteriores, se considera un error léxico y se registra en la lista `errores_List` con detalles como el carácter, el tipo de error y la posición.
    
7.  Se ajustan las variables `cadena`, `puntero`, `f`, `c`, y `tokens` según lo que se haya procesado.

### - Función find_STR

se utiliza para encontrar una cadena delimitada por comillas dobles (`" "`) dentro de un texto. A continuación, se proporciona una explicación general de cómo funciona esta función:

-   **Parámetros de Entrada:** La función toma como parámetro `texto`, que es la porción de texto en la que se busca la cadena delimitada por comillas dobles.
    
-   **Inicialización de Variables:** Se inicializan dos variables, `lexema` y `clave`.
    
    -   `lexema` se utiliza para almacenar la cadena encontrada, excluyendo las comillas dobles.
    -   `clave` se utiliza para rastrear el progreso al recorrer el texto.
-   **Bucle de Iteración:** La función itera a través de cada carácter en el `texto` proporcionado utilizando un bucle `for`.
    
-   **Verificación de Caracteres:** Para cada carácter en el texto, se obtiene su valor ASCII mediante `ord(caracter)` y se almacena en la variable `ascii`. Además, se agrega el carácter a la variable `clave` para llevar un registro de los caracteres que se han procesado.
    
-   **Búsqueda de Comillas Dobles:** Se verifica si el valor ASCII del carácter es igual a 34, lo que indica que se ha encontrado una comilla doble (`"`). Si se encuentra una comilla doble, se considera que la cadena ha sido delimitada y se devuelve el `lexema` encontrado y el texto restante después de la comilla doble.
    
-   **Construcción del Lexema:** Mientras no se encuentre una comilla doble, se continúa construyendo el `lexema` agregando cada carácter al `lexema`.
    
-   **Retorno de Resultados:** Si no se encuentra una comilla doble en el `texto`, la función devuelve `None` tanto para el `lexema` como para el texto restante.

### - Función find_Number

Se utiliza para encontrar y analizar números (tanto enteros como decimales) en un texto proporcionado. A continuación, se proporciona una explicación general de cómo funciona esta función:

-   **Parámetros de Entrada:** La función toma como parámetro `texto`, que es la porción de texto en la que se busca un número.
    
-   **Inicialización de Variables:** Se inicializan varias variables:
    
    -   `numero`: Se utiliza para construir el número encontrado.
    -   `clave`: Se utiliza para rastrear el progreso al recorrer el texto.
    -   `verificar`: Es una bandera booleana que indica si se ha encontrado un punto decimal en el número.
-   **Bucle de Iteración:** La función itera a través de cada carácter en el `texto` proporcionado utilizando un bucle `for`.
    
-   **Verificación de Caracteres:** Para cada carácter en el texto, se obtiene su valor ASCII mediante `ord(caracter)` y se almacena en la variable `ascii`. Además, se agrega el carácter a la variable `clave` para llevar un registro de los caracteres que se han procesado.
    
-   **Identificación de Números:** Se verifica si el carácter actual es un punto decimal (ASCII 46), un signo negativo (ASCII 45) o un dígito mediante condiciones `if`. Si es alguno de estos casos, se agrega el carácter al `numero`.
    
-   **Manejo de Números Decimales:** Si se encuentra un punto decimal en el número (`verificar` es `True`), se considera que el número es decimal y se convierte a tipo de dato `float`. Se devuelve el número decimal y el texto restante después del número.
    
-   **Manejo de Números Enteros:** Si no se encuentra un punto decimal en el número, se considera que el número es entero y se convierte a tipo de dato `int`. Se devuelve el número entero y el texto restante después del número.
    
-   **Retorno de Resultados:** Si no se encuentra ningún número en el `texto`, la función devuelve `None` tanto para el número como para el texto restante.  