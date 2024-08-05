import geopandas as gpd
import zipfile
import os

# Función que convierte un archivo shapefile (.shp) a un archivo KML (.kml)
def shp2kml(shp_path, kml_path='output_file.kml'):
    """
    Convierte un archivo Shapefile a un archivo KML.
    
    Parámetros:
    - shp_path: Ruta del archivo Shapefile de entrada.
    - kml_path: Ruta del archivo KML de salida (opcional, por defecto es 'output_file.kml').
    """
    # Lee el archivo Shapefile usando Geopandas y lo carga en un GeoDataFrame
    gdf = gpd.read_file(shp_path)
    # Guarda el GeoDataFrame como un archivo KML
    gdf.to_file(kml_path, driver='KML')
    # Devuelve el GeoDataFrame
    return gdf

# Función que convierte un archivo shapefile (.shp) a un archivo KMZ (.kmz)
def shp2kmz(shp_path, kmz_path='output_file.kmz'):
    """
    Convierte un archivo Shapefile a un archivo KMZ.
    
    Parámetros:
    - shp_path: Ruta del archivo Shapefile de entrada.
    - kmz_path: Ruta del archivo KMZ de salida (opcional, por defecto es 'output_file.kmz').
    """
    # Define el nombre temporal del archivo KML
    temp_kml = 'temp.kml'
    # Convierte el archivo Shapefile a KML temporal
    shp2kml(shp_path, temp_kml)
    
    # Crea el archivo KMZ a partir del archivo KML temporal
    with zipfile.ZipFile(kmz_path, 'w', zipfile.ZIP_DEFLATED) as kmz:
        kmz.write(temp_kml, os.path.basename(temp_kml))
    
    # Elimina el archivo KML temporal
    os.remove(temp_kml)

# Escribir la ruta del archivo .shp a convertir
shp_path = "PruebaRecorte1/poligono1.shp"

# Llama a la función para convertir el archivo shapefile a KML
shp2kml(shp_path, 'output_file.kml')

# Llama a la función para convertir el archivo shapefile a KMZ
shp2kmz(shp_path, 'output_file.kmz')
