

def api_aemet(api_key, estacion, anioini,aniofin):
    
''' Esta función realiza la solicitud a la API de AEMET de los valores de clima normales por estación
    meteorológica. Descarga un archivo .json

    Previamente deberá solicitar la api-key en la página de la API AEMET.

    Importaciones necesarias; bliblioteca requests

    Introducir los valores de la función como string.'''

    
    key = {"api_key":f"{api_key}"}

    headers = {'cache-control': "no-cache"}
    
    url = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/mensualesanuales/datos/anioini/{anioini}/aniofin/{aniofin}/estacion/{estacion}"

    response = requests.get(url, headers=headers, params=key)

    s_url = response.json()['datos']

    response = requests.get(s_url)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        
        # Guardar la respuesta en un archivo local
        with open(f'datos_aemet_{estacion}.json', 'wb') as f:
            f.write(response.content)
        print("Datos descargados y guardados correctamente.")
    else:
        print("Error al descargar los datos.")





#Función para sustituir las comas por los puntos en todos los valores de un DF

def cambiar_comas_por_puntos(df):
    # Función para cambiar las comas por puntos en un valor

    '''La función sustituir es la que entra un valor de celda, mira si es string y si tiene coma
    lo cambia por punto.
    
    La función superior cambiar_como _por_puntos es solo para que la función sustituir se aplique
    a todas las columnas del DF.'''
    
    def sustituir(val):
        if isinstance(val, str):
            return val.replace(',', '.')
        return val

    # Aplicar la función de sustitución a cada columna
    for columna in df.columns:
        df[columna] = df[columna].apply(sustituir)

    return df