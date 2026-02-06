def buscar_archivo(carpeta, archivo):
    # Recorremos cada elemento de la carpeta
    for elemento in carpeta:
        if isinstance(elemento, dict):
            # Si es una subcarpeta, entramos de forma recursiva
            if buscar_archivo(elemento["contenido"], archivo):
                return True
        else:
            # Si es un archivo
            if elemento == archivo:
                return True
    return False


# Simulación de carpetas y archivos
sistema = [
    "tarea.docx",
    "foto.jpg",
    {
        "nombre": "Documentos",
        "contenido": [
            "cv.pdf",
            {
                "nombre": "Escuela",
                "contenido": [
                    "proyecto.py",
                    "examen.pdf"
                ]
            }
        ]
    }
]

archivo_buscado = "proyecto.py"

if buscar_archivo(sistema, archivo_buscado):
    print("Archivo encontrado")
else:
    print("Archivo no encontrado")
