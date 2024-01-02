import os

def concatenar_archivos_txt(carpeta_entrada, archivo_salida):
    # Obtener la lista de archivos en la carpeta de entrada
    archivos_txt = [archivo for archivo in os.listdir(carpeta_entrada) if archivo.endswith(".txt")]

    # Verificar si hay archivos para concatenar
    if not archivos_txt:
        print("No hay archivos TXT en la carpeta especificada.")
        return

    # Crear o sobrescribir el archivo de salida
    with open(archivo_salida, 'w') as salida:
        # Iterar sobre cada archivo y concatenar su contenido
        for archivo_txt in archivos_txt:
            ruta_completa = os.path.join(carpeta_entrada, archivo_txt)
            with open(ruta_completa, 'r') as archivo_entrada:
                contenido = archivo_entrada.read()
                salida.write(contenido)
                salida.write('\n')  # Agregar un salto de línea entre archivos

    print(f"Se han concatenado {len(archivos_txt)} archivos en {archivo_salida}.")

# Especifica la carpeta de entrada y el archivo de salida
carpeta_entrada = 'español/txt_limpio'
archivo_salida = 'concatenacion.txt'

# Llama a la función para concatenar los archivos
concatenar_archivos_txt(carpeta_entrada, archivo_salida)
