import geopandas as gpd

def kml2shp(kml_path, shp_path='output_file.shp'):
    """
    Convierte un archivo KML a un archivo Shapefile.
    
    Parámetros:
    - kml_path: Ruta del archivo KML de entrada.
    - shp_path: Ruta del archivo Shapefile de salida (opcional, por defecto es 'output_file.shp').
    """
    # Lee el archivo KML usando Geopandas y lo carga en un GeoDataFrame
    gdf = gpd.read_file(kml_path, driver='KML')
    # Guarda el GeoDataFrame como un archivo Shapefile
    gdf.to_file(shp_path, driver='ESRI Shapefile')
    # Devuelve el GeoDataFrame
    return gdf

# Escribir la ruta del archivo .kml a convertir
kml_path = "path/to/input_file.kml"

# Llama a la función para convertir el archivo KML a Shapefile
kml2shp(kml_path, 'output_file.shp')
