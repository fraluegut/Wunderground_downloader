# Proyecto WunderData
Este proyecto se enfoca en descargar y procesar datos meteorológicos de la página web Weather Underground utilizando la biblioteca requests para hacer peticiones web y pandas para procesar los datos en un DataFrame.

## Clase WunderData
La clase WunderData tiene dos atributos, start_date y end_date, que indican el rango de fechas para el cual se desean descargar los datos. El método download_data realiza una petición a la página web de Weather Underground utilizando el rango de fechas especificado y devuelve los datos en un DataFrame de pandas.

## Clase RangoFechas
La clase RangoFechas tiene un atributo dia_mes, que es una cadena en el formato "YYYY-MM" que indica el año y el mes para el cual se desean obtener los días. El método convert_to_year convierte el año en el formato "YYYY" a entero y el método convert_to_month convierte el mes en el formato "MM" a entero. El método first_and_last_day_of_month utiliza los métodos anteriores para obtener el primer y último día del mes especificado.

### Pruebas unitarias
Se incluyen pruebas unitarias con el framework pytest para verificar que la clase WunderData y RangoFechas están funcionando correctamente. Estas pruebas se aseguran de que los métodos de las clases devuelven los resultados esperados y que el rango de fechas especificado es correcto.