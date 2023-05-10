# CacheArquiDowOrduz
## Parcial practico, arquitectura del computador.

## Arquitectura del sistema de cache:

### Tamaño de bloque: 8 bytes
### Total de bloques en cache: 32
### Conjuntos: 16
### Vías asociativas: 2
### Política de reemplazo: FIFO (el bloque más antiguo en la vía seleccionada es reemplazado)
### Política de escritura: Write Back (los datos se escriben en la cache y se marcan como "modificados", pero no se escriben en la memoria ### principal hasta que el bloque sea reemplazado)

## Maquina De Estados

### Estado 1: Esperar dirección de memoria.
### Transición: Recibir dirección de memoria.

### Estado 2: Decodificar dirección de memoria.
### Transición: Identificar conjunto y etiqueta correspondientes.

### Estado 3: Buscar etiqueta en ambas vías del conjunto.
### Transición A: Etiqueta encontrada en alguna de las vías (hit).
### Acciones:

### Actualizar contador de hits.
### Si la operación es de escritura, marcar el bloque como modificado.
### Leer o escribir datos en la caché según corresponda.
### Transición B: Etiqueta no encontrada en ninguna de las vías (miss).
### Acciones:

### Actualizar contador de misses.
### Seleccionar el bloque más antiguo en la vía correspondiente (política FIFO).
### Si el bloque está modificado, escribir los datos en la memoria principal.
### Cargar los datos correspondientes al bloque desde la memoria principal.
### Marcar el bloque como válido y cargar la etiqueta y los datos correspondientes.
### Si la operación es de escritura, marcar el bloque como modificado.
### Leer o escribir datos en la caché según corresponda.
### Estado 4: Esperar siguiente operación de memoria.
### Transición: Recibir siguiente operación de memoria.

### Estado 5: Verificar final de la memoria principal.
### Transición A: Fin de la memoria principal alcanzado.
### Acciones:

### Terminar la ejecución.
### Mostrar los resultados (contador de hits, contador de misses, archivos TXT de RAM sin modificar y modificada, y memoria caché).
### Transición B: Continuar con la siguiente dirección de memoria.
### Transición al Estado 2.
