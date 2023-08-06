# Proyecto_ETL_Precipitaciones

Descripción del proyecto:

Se ha recogido una muestra de provincias de España a partir de una tabla con datos de los municipios de España descargada desde la fuente Kaggle.

Se ha enriquecido la muestra con valores climatológicos y de tipos de explotaciones agrarias para estudiar una relación entre el tipo de agricultura en cada provincia de nuestra muestra y los valores de precipitación media de estas.

Procedimiento:

A partir de una base de datos completa de los municipios españoles y datos correspondientes al censo de habitantes y superficie, se ha optado por recoger una muestra aleatoria de provincias para nuestro análisis.

A partir de ella se ha enriquecido el dato con valores climatológicos normales descargados desde la API de la Agencia estatal de meteorología (AEMET), donde se han obtenido valores como; precipitaciones medias, temperaturas, nubosidad... Posteriorme se han limpiado los datos y estrycturado las tablas para ser homogeneas.

Se han obtenido, además, datos del último censo de explotaciones agrarias de nuestra muestra para poder compararlas después con nuestros valores de precipitaciones. Se han limpiado y estructurado también esta tabla.

Para la obtención de la información de la API de AEMET, se ha utilizado la biblioteca requests para hacer la solicitud y se han limpiado las tablas con pandas.

Se crea una base de datos SQL para contener toda la información de manera estructurada y a la que hemos relizado las consultas para el posterior análisis.

Finalmente, se ha realizado un análisis gráfico para ver la relación entre las precipitaciones por provincia y ella distribución del tipo de explotación agraria.

Estructura de los datos:

Se han creado varias carpetas donde se contienen los datos de la tablas descargadas, las tablas limpiadas y notebooks de limpieza y análisis de datos.

- Carpeta data; contiene las tablas descargadas desde las fuentas, así como las tablas limpias con las se  han relaizado los análisis. Contiene tambie imágenes del análisis.

- Carpeta notebooks; contiene los archivos de jupyter notebooks donde está la solicitud a la API de AEMET, las limpieza de las tablas y el análisis final. También hay un archivo .py donde encontrás las funciones utilizadas para limpieza y nuestra request.

- Carpeta sql; contiene las queries para la creación de la base de datos y las necesarias para exportar tablas que nos servirían para nuestro análisis final.

Fuentes:

API AEMET
KAGGLE
INE

