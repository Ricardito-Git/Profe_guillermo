def buscar_archivo(carpeta, archivo):
    
    for elemento in carpeta:
        if isinstance(elemento, dict):
            
            if buscar_archivo(elemento["contenido"], archivo):
                return True
        else:
            
            if elemento == archivo:
                return True
    return False



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

