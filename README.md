<h1 align="center"> Proyecto_ETL_Precipitaciones </h1>

<h1 align="center">![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/img_portada.jpeg) </h1>

Proyecto 3 como Analista de datos en IronHack Madrid.

## Descripción del proyecto:

Se ha recogido una muestra de provincias de España a partir de una tabla con datos de los municipios de España, descargada desde la fuente Kaggle.

Se ha enriquecido la muestra con valores climatológicos y de tipos de explotaciones agrarias para estudiar una relación entre el tipo de agricultura en cada provincia de nuestra muestra y los valores de precipitación media de estas.

## Procedimiento:

A partir de una base de datos completa de los municipios españoles y datos correspondientes al censo de habitantes y superficie, se ha optado por recoger una muestra aleatoria de provincias para nuestro análisis.

A partir de ella se ha enriquecido el dato con valores climatológicos normales descargados desde la API de la Agencia estatal de meteorología (AEMET), donde se han obtenido valores como; precipitaciones medias, temperaturas, nubosidad... Posteriorme se han limpiado los datos y estructurado las tablas para ser homogéneas.

Se han obtenido, además, datos del último censo de explotaciones agrarias de nuestra muestra para poder compararlas después con nuestros valores de precipitaciones. Se ha limpiado, y estructurado también, esta tabla.

Para la obtención de la información de la API de AEMET, se ha utilizado la biblioteca requests para hacer la solicitud y se han limpiado las tablas con pandas.

Se crea una base de datos SQL para contener toda la información de manera estructurada y a la que hemos relizado las consultas para el posterior análisis.

Finalmente, se ha realizado un análisis gráfico para ver la relación entre las precipitaciones por provincia y la distribución del tipo de explotación agraria.

## Estructura de los datos:

Se han creado varias carpetas donde se contienen los datos de la tablas descargadas, las tablas limpiadas y notebooks de limpieza y análisis de datos.

- Carpeta data; contiene las tablas descargadas desde las fuentas, así como las tablas limpias con las se  han relaizado los análisis. Contiene tambie imágenes del análisis.

- Carpeta notebooks; contiene los archivos de jupyter notebooks donde está la solicitud a la API de AEMET, las limpieza de las tablas y el análisis final. También hay un archivo .py donde encontrás las funciones utilizadas para limpieza y nuestra request.

- Carpeta sql; contiene las queries para la creación de la base de datos y las necesarias para exportar tablas que nos servirían para nuestro análisis final.

## Visualización:

Vamos a observar primero la evolución de la precipitación media mensual en cada una de las provincias de nuestra muestra.


![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/prec_19-22_cadiz.png)

![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/prec_19-22_huelva.png)

![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/prec_19-22_girona.png)

![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/prec_19-22_almeria.png)

![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/prec_19-22_coruna.png)

Observamos que la diferencia de precipitaciones entre las provincias del norte y sur del país son considerables, dejando al lado algunos picos que podemos ver en Cádiz. Las provincias de Cádiz y Huelva presentan valores altos en momentos puntuales del tiempo, sin embargo Almería presenta valores bajos durante todo el tiempo estudiado. En el norte la lluvia es más constante. Vamos a verlo mejor en una misma gráfica durante el año 2020.

![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/prec_2020_muestra.png)

Vamos a ver ahora una comparativa entre el tipo de explotación agrícola predominante en Girona (donde hay gran niveles altos de precipitaciones) y Almería (que presenta los niveles más bajos). Datos recogidos del censo de 2020.

![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/tipos_cultivo_girona.png)

![Image](https://github.com/borjadola/Proyecto_ETC_Precipitaciones/blob/main/data/imagenes/tipos_cultivo_almeria.png)

Podemos ver que los cultivos de invernadero y de tipo leñoso son un tipo de cultivo considerable en  Almería a diferencia de Girona. Se intuye que es debido a la alta radiación solar y las bajas precipitaciones, siendo un cultivo donde existe un aprovechamiento mayor del agua en el caso de invernaderos, y que depende menos de las precipitaciones.

## Fuentes:

[API AEMET](https://opendata.aemet.es/centrodedescargas/inicio)

[KAGGLE](https://www.kaggle.com/datasets/fcojavt/municipios-spain)

[INE](https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736176851&menu=ultiDatos&idp=1254735727106)

