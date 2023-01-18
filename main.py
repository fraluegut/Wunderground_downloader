import requests
from bs4 import BeautifulSoup
import pandas as pd

# Fecha de inicio y final (en formato "YYYY-MM-DD")
start_date = "2022-01-01"
end_date = "2022-01-31"

# URL de la página web
url = "https://wu-next-ibm.wunderground.com/dashboard/pws/IELCUE1/table/" + str(start_date) + "/" + str(end_date) + "/monthly/"

# Realizar la petición a la página web y obtener el HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Obtener los datos de la segunda tabla
table = soup.find_all("table")[3]
rows = table.find_all("tr")
data = []
for row in rows:
    cols = row.find_all("td")
    cols = [col.text for col in cols]
    data.append(cols)

# Crear el DataFrame con los datos obtenidos
df = pd.DataFrame(data)

# Mostrar el DataFrame
print(df)