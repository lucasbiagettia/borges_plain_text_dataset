def eliminar_fragmento_numero(linea):
    import re
    return re.sub(r'\[\d+\]', '', linea)

def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        for linea in entrada:
            linea_sin_fragmento = eliminar_fragmento_numero(linea)
            salida.write(linea_sin_fragmento)

if __name__ == "__main__":
    archivo_entrada = "español/txt_limpio/Jorge Luis Borges - Otras inquisiciones (2015).txt"
    archivo_salida = "español/txt_limpio/Jorge Luis Borges - Otras inquisiciones (2015).txt"

    try:
        procesar_archivo(archivo_entrada, archivo_salida)
        print(f"El archivo '{archivo_entrada}' ha sido procesado y el resultado se ha guardado en '{archivo_salida}'.")
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo_entrada}' no fue encontrado.")
    except Exception as e:
        print(f"Error inesperado: {e}")
