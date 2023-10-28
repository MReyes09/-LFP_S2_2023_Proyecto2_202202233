#####  Universidad de San Carlos de Guatemala
#####  Facultad de Ingeniería
#####  Escuela de Ciencias y Sistemas
#####  Laboratorio de Lenguajes Formales y de Programación
##### **Matthew Emmanuel Reyes Melgar 202202233**

# Manual De Usuario

## Descripción General

El Manual de Usuario proporciona una guía detallada sobre el uso de la Aplicación de Análisis Léxico y Sintactico. Esta aplicación consta de una ventana única que ofrece opciones para cargar, editar, analizar y generar informes sobre el código fuente en un lenguaje específico. A continuación, se describe en detalle cada componente y función de la aplicación.

## Vista de Usuario

La vista de usuario de la aplicación consta de una ventana principal con los siguientes elementos:

### Barra de Navegación

La barra de navegación se encuentra en la parte superior de la ventana y contiene las siguientes opciones:

- **Abrir:** Permite al usuario abrir un archivo en formato BIZDATA para editarlo en la aplicación.
- **Analizar:** Permite al usuario analizar el archivo y así ejecutar las funciones, operaciones y verificar posibles errores.
- **Tokens:** Permite al usuario poder optener un HTML donde se muestran todos los caracteres reconocidos al analizar.
- **Errores:** Permite al usuario poder optener un HTML donde se muestran todos los errores encontrados al analizar.

### Área de Edición de Texto (txtArea)

El área de edición de texto es un campo de texto grande donde se muestra y edita el contenido del archivo BIZDATA cargado. El usuario puede modificar el código fuente en este campo.

### Consola (txtArea)

Es un area donde unicamente sirve para ver los resultados de las funciones que se encuentran en el archivo BIZDATA, esto se podrá ver al
analizar el documento con anterioridad.

## Uso Básico

A continuación, se describen las funciones básicas de la aplicación:

### Abrir

La opción "Abrir" en la barra de navegación permite al usuario seleccionar y cargar un archivo BIZDATA existente en la aplicación. El contenido del archivo se muestra en el área de edición de texto (txtArea) y se puede editar.

### Analizar

El botón "Analizar" ejecuta el analizador léxico y sintátctico en el código fuente cargado en el área de edición de texto. Después de la ejecución, se muestran los resultados de las operaciones contenidas en el archivo BIZDATA en un cuadro de mensaje. Los resultados incluyen la identificación de tokens y operaciones realizadas, esta se ve reflejada en otra area de texto el cual es la consola.

### Errores

Genera un archivo HTML separado que muestra los errores léxicos y sintacticos detectados en el código fuente. Si no se encuentran errores, el archivo HTML estará vacío. Los errores incluyen detalles como el token, el tipo de error, la columna y la fila en la que se produjo el error.

## Funcionalidades Adicionales

### Reporte

La funcionalidad del botón "Reporte" aún no ha sido definida en la aplicación y puede implementarse en futuras versiones.



## Conclusiones

El Manual de Usuario proporciona una guía completa para utilizar la Aplicación de Análisis Léxico y sintactico. Los usuarios pueden cargar, editar y analizar código fuente, así como generar informes y gestionar errores léxicos y sintacticos. La aplicación ofrece una interfaz sencilla y funcionalidades esenciales para el análisis de código en un lenguaje específico.

