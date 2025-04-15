import pytest

from app.main import outdated_products
from unittest import mock
from typing import Any
import datetime


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


@mock.patch("app.main.datetime")
def test_today_date_not_outdated(mock_datetime: mock,
                                 products_list: Any) -> None:
    mock_datetime.date.today.return_value = datetime.date(2020, 12, 12)
    assert outdated_products(products_list) == ["sausages"]


@mock.patch("app.main.datetime")
def test_yesterday_is_outdated(mock_datetime: mock,
                               products_list: Any) -> None:
    mock_datetime.date.today.return_value = datetime.date(2025, 5, 25)
    products_list[0]["expiration_date"] = datetime.date(2025, 5, 24)
    assert outdated_products(products_list) == ["milk", "sausages"]
