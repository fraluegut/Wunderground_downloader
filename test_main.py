from datetime import datetime
import datetime

import pandas as pd

from main import Fechas, WunderData, RangoFechas
import pytest

def test_Fechas_get_intermediate_months():
    # Test con fecha inicial y final iguales
    fechas = Fechas(1, 2020, 1, 2020)
    assert fechas.get_intermediate_months() == ["2020-01"]

    # Test con fecha inicial y final en el mismo año
    fechas = Fechas(1, 2020, 4, 2020)
    assert fechas.get_intermediate_months() == ["2020-01", "2020-02", "2020-03", "2020-04"]

    # Test con fecha inicial y final en diferentes años
    fechas = Fechas(10, 2020, 2, 2021)
    assert fechas.get_intermediate_months() == ["2020-10", "2020-11", "2020-12", "2021-01", "2021-02"]


@pytest.fixture
def rf():
    return RangoFechas("2022-01")

def test_convert_to_year(rf):
    assert rf.convert_to_year() == 2022

def test_convert_to_month(rf):
    assert rf.convert_to_month() == 1

def test_first_and_last_day_of_month(rf):
    first_day, last_day = rf.first_and_last_day_of_month()
    assert first_day == datetime.date(2022, 1, 1)
    assert last_day == datetime.date(2022, 2, 1) + datetime.timedelta(days=-1)


@pytest.fixture
def wd():
    start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d")
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return WunderData(start_date, end_date)

def test_download_data(wd):
    # Test that the download_data method returns a DataFrame
    result = wd.download_data()
    assert isinstance(result, pd.DataFrame)

def test_data_format(wd):
    # Test that the data returned is in the correct format
    result = wd.download_data()
    assert result.shape[0] > 0  # check that there are more than 0 rows in the DataFrame
    assert result.shape[1] > 0  # check that there are more than 0 columns in the DataFrame
