# Descripción del programa TextFormatter

Este repositorio contiene un script en Python que proporciona funcionalidades para leer, formatear, escribir y eliminar archivos de texto. Las principales características de este script incluyen:

1. Leer Archivo: Lee el contenido de un archivo de texto especificado y lo devuelve como una cadena única.
2. Escribir Archivo: Escribe un texto dado en un archivo especificado.
3. Justificación de Texto: Justifica el texto para que se ajuste a un ancho máximo especificado, utilizando programación dinámica para determinar la mejor manera de dividir el texto en líneas.
4. Eliminar Archivo: Elimina un archivo de texto especificado.
5. Interfaz Interactiva de Línea de Comandos: Permite a los usuarios elegir interactivamente entre las diferentes operaciones mencionadas.

## Funciones del programa

 - format_text(text: str, max_width: str) -> list[str]: Justifica el texto dado para que se ajuste al ancho máximo especificado.
 - read_file(archive_path: str) -> str: Lee el texto de un archivo específico.
 - write(archive_path: str, text: str) -> None: Escribe un texto específico en un archivo.
 - delete(archive_path: str) -> None: Elimina un archivo específico.
 - main() -> None: Proporciona una interfaz de línea de comandos para que los usuarios interactúen con el script.
