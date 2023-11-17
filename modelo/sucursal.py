import csv
import os
ruta_archivo_sucursales=''



def exportar_a_csv():
    """
    Exporta los datos de sucursales a un archivo CSV.
    """
    with open(ruta_archivo_sucursales, 'w', newline='') as csvfile:
        campo_nombres = ['id', 'nombre de sucursal', 'contraseña_admin','ciudad']
        writer = csv.DictWriter(csvfile, fieldnames=campo_nombres)
        writer.writeheader()
        for sucursal in sucursales:
            writer.writerow(sucursal)

def importar_datos_desde_csv():
    """
    Importa los datos de sucursales desde un archivo CSV.
    """
    global sucursales
    global id_sucursal
    sucursales = []  # Limpiamos la lista de sucursales antes de importar desde el archivo CSV
    with open(ruta_archivo_sucursales, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Convertimos el ID de cadena a entero
            row['id'] = int(row['id'])
            sucursales.append(row) 
    if len(sucursales)>0:
        id_sucursal= sucursales[-1]["id"]+1
    else:
        id_sucursal = 1