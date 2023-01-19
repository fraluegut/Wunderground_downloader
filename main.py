import requests
from bs4 import BeautifulSoup
import pandas as pd
from dataclasses import dataclass
import datetime
from datetime import date

# Clase Fechas:
# Contiene los atributos start_month, start_year, end_month y end_year
# y un método get_intermediate_months que devuelve una lista de meses intermedios entre start_month y start_year y end_month y end_year
@dataclass()
class Fechas:
    start_month: int
    start_year: int
    end_month: int
    end_year: int

    # Función lambda que devuelve una lista de meses intermedios entre start_month y start_year y end_month y end_year
    # def get_intermediate_months(self):
    #     get_intermediate_months = lambda start_month, start_year, end_month, end_year: [
    #         (date(y, m, 1).strftime('%Y-%m') if m != 12 else date(y + 1, 1, 1).strftime('%Y-%m')) for y in
    #         range(start_year, end_year + 1) for m in range(start_month, 13) if
    #         y == end_year and m <= end_month or y != end_year]
    #     intermediate_months = get_intermediate_months(start_month, start_year, end_month, end_year)
    #     return intermediate_months

    def get_intermediate_months(self):
        intermediate_months = []
        for year in range(self.start_year, self.end_year + 1):
            start_month = self.start_month if year == self.start_year else 1
            end_month = self.end_month if year == self.end_year else 12
            for month in range(start_month, end_month + 1):
                intermediate_months.append(f"{year}-{month:02d}")
        return intermediate_months

# Clase WunderData:
# Contiene los atributos start_date, end_date y url
# y un método download_data que descarga los datos de la url y los devuelve en un DataFrame
@dataclass
class WunderData:
    start_date: str
    end_date: str
    # Método para descargar datos de la página web y devolverlos en un DataFrame
    def download_data(self):
        url = f"https://wu-next-ibm.wunderground.com/dashboard/pws/IELCUE1/table/{self.start_date}/{self.end_date}/monthly/"

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
        print(df)
        return df
@dataclass()
class RangoFechas:
    dia_mes: str

    def convert_to_year(self):
        year = int(self.dia_mes.split("-")[0])
        return year

    def convert_to_month(self):
        month = int(self.dia_mes.split("-")[1])
        return month


    def first_and_last_day_of_month(self):
        self.year = self.convert_to_year()
        self.month = self.convert_to_month()
        # Obtener el primer día del mes
        first_day = datetime.date(self.year, self.month, 1)
        # print("Primer dia del mes: ", first_day)

        # Obtener el último día del mes
        last_day = datetime.date(self.year, self.month+1, 1) + datetime.timedelta(days=-1)
        # last_day = last_day.replace(day=28) + datetime.timedelta(days=last_day.month)
        # print("Ultimo dia del mes: ", last_day)
        return first_day, last_day

if __name__ == "__main__":
    print("Iniciando")
    # wunder_data_object = WunderData()
    # df = wunder_data_object.download_data()
    # print(df)

    # Ejemplo de uso
    start_month = 1
    start_year = 2021
    end_month = 12
    end_year = 2021
    fechas = Fechas(start_month, start_year, end_month, end_year)
    periodo = fechas.get_intermediate_months()
    print("Periodo")
    print(periodo)
    for month in range(len(periodo)):
        print("Mes")
        print(month)

        fecha = RangoFechas(periodo[month])
        first_day, last_day = fecha.first_and_last_day_of_month()
        print(last_day)
        wunder_value = WunderData(first_day, last_day)
        wunder_value.download_data()