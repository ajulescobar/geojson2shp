import geopandas as gpd

# Función que convierte un archivo GeoJSON a un archivo shapefile (.shp)
def gjs2shp(gj_path):
    # Lee el archivo GeoJSON usando Geopandas y lo carga en un GeoDataFrame
    gdf = gpd.read_file(gj_path)
    # Guarda el GeoDataFrame como un archivo shapefile
    gdf.to_file('file.shp')
    # Devuelve el GeoDataFrame
    return gdf

# Escribir la ruta del archivo .GeoJSON a convertir
gj_path="myJson.geojson"
# Llama a la función para convertir el archivo GeoJSON a shapefile
gjs2shp(gj_path)
