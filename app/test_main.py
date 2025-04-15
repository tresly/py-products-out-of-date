from freezegun import freeze_time
import pytest
import datetime
from app.main import outdated_products


@pytest.fixture()
def products_list() -> list:
    return [
        {
            "name": "milk",
            "expiration_date": datetime.date(2020, 12, 12),
            "price": 100
        },
        {
            "name": "sausages",
            "expiration_date": datetime.date(2019, 12, 5),
            "price": 70
        }
    ]


@freeze_time("2020-12-12")
def test_today_date_not_outdated(products_list):
    assert outdated_products(products_list) == ["sausages"]


@freeze_time("2025-05-25")
def test_yesterday_is_outdated(products_list):
    products_list[0]["expiration_date"] = datetime.date(2025, 5, 24)
    assert outdated_products(products_list) == ["milk", "sausages"]
