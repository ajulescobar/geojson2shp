import geopandas

# Función que convierte un archivo shapefile (.shp) a un archivo GeoJSON (.geojson)
def shp2gjs(shp_path):
    # Lee el archivo shapefile usando Geopandas y lo carga en un GeoDataFrame
    myshpfile = geopandas.read_file(shp_path)
    # Guarda el GeoDataFrame como un archivo GeoJSON
    myshpfile.to_file('myJson.geojson', driver='GeoJSON')
    # Devuelve el GeoDataFrame
    return myshpfile

# Escribir la ruta del archivo .shp a convertir
shp_path = "PruebaRecorte1/poligono1.shp"
# Llama a la función para convertir el archivo shapefile a GeoJSON
shp2gjs(shp_path)
