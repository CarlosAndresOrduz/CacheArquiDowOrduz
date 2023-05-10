# Simulador de Memoria Caché Asociativa por Conjuntos de 2 Vías FIFO Write Back

### Sebastián Dow Valenzuela / Carlos Andrés Orduz Guacaneme

Este es un simulador en Python de una memoria caché asociativa por conjuntos de 2 vías con política de reemplazo FIFO y escritura diferida (write back). El objetivo de este proyecto es proporcionar una implementación funcional de una memoria caché que pueda ser utilizada para analizar y evaluar su rendimiento en diferentes escenarios.

## Arquitectura del sistema de caché

La arquitectura del sistema de caché utilizada en este simulador es la siguiente:

- Tamaño de bloque: 8 bytes
- Total de bloques en la caché: 32
- Conjuntos: 16
- Vías asociativas: 2
- Política de reemplazo: FIFO (el bloque más antiguo en la vía seleccionada es reemplazado)
- Política de escritura: Write Back (los datos se escriben en la caché y se marcan como "modificados", pero no se escriben en la memoria principal hasta que el bloque sea reemplazado)

## Máquina de Estados

El simulador utiliza una máquina de estados con los siguientes estados y transiciones:

Estado 1: Esperar dirección de memoria.
Transición: Recibir dirección de memoria.

Estado 2: Decodificar dirección de memoria.
Transición: Identificar conjunto y etiqueta correspondientes.

Estado 3: Buscar etiqueta en ambas vías del conjunto.
Transición A: Etiqueta encontrada en alguna de las vías (hit).
Acciones:

- Actualizar contador de hits.
- Si la operación es de escritura, marcar el bloque como modificado.
- Leer o escribir datos en la caché según corresponda.

Transición B: Etiqueta no encontrada en ninguna de las vías (miss).
Acciones:

- Actualizar contador de misses.
- Seleccionar el bloque más antiguo en la vía correspondiente (política FIFO).
- Si el bloque está modificado, escribir los datos en la memoria principal.
- Cargar los datos correspondientes al bloque desde la memoria principal.
- Marcar el bloque como válido y cargar la etiqueta y los datos correspondientes.
- Si la operación es de escritura, marcar el bloque como modificado.
- Leer o escribir datos en la caché según corresponda.

Estado 4: Esperar siguiente operación de memoria.
Transición: Recibir siguiente operación de memoria.

Estado 5: Verificar final de la memoria principal.
Transición A: Fin de la memoria principal alcanzado.
Acciones:
- Terminar la ejecución.
- Mostrar los resultados (contador de hits, contador de misses, archivos TXT de RAM sin modificar y modificada, y memoria caché).

Transición B: Continuar con la siguiente dirección de memoria.
Transición al Estado 2.

## Características principales

- Memoria caché asociativa por conjuntos de 2 vías FIFO con escritura diferida (write back).
- Tamaño configurable de la memoria caché.
- Número de conjuntos configurable.
- Política de reemplazo FIFO (First-In, First-Out).
- Implementación en lenguaje Python.

## Requisitos previos

Asegúrate de tener los siguientes requisitos previos antes de ejecutar el simulador:

- Python 3 instalado en tu sistema.

## Uso

1. Clona el repositorio o descarga los archivos del simulador.

2. Abre una terminal y navega hasta el directorio donde se encuentran los archivos del simulador.

3. Ejecuta el siguiente comando para iniciar el simulador: python cache_simulator.py

4. Sigue las instrucciones en pantalla para configurar los parámetros de la memoria caché y realizar las operaciones de lectura y escritura.

*La entrada del programa corresponde a los datos almacenados en una meroria RAM y sus respectivas direcciones como paraece en el modelo de testram.txt* 

## Configuración de la memoria caché

Antes de ejecutar el simulador, puedes ajustar la configuración de la memoria caché editando el archivo `cache_config.py`. En este archivo, puedes modificar los siguientes parámetros:

- Tamaño de bloque: Especifica el tamaño de bloque deseado en bytes. Por defecto, el tamaño de bloque es 8 bytes.

- Total de bloques en caché: Especifica el número total de bloques en la caché. Por defecto, la caché tiene 32 bloques.

- Conjuntos: Especifica el número de conjuntos en la caché. Por defecto, la caché tiene 16 conjuntos.

- Vías asociativas: Especifica el número de vías asociativas en cada conjunto. Por defecto, la caché tiene 2 vías asociativas.

- Política de reemplazo: Especifica la política de reemplazo a utilizar. Por defecto, se utiliza la política FIFO (First-In, First-Out).

- Política de escritura: Especifica la política de escritura a utilizar. Por defecto, se utiliza la política Write Back.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o tienes alguna mejora para el simulador, por favor, crea un *issue* o envía una *pull request*.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.



