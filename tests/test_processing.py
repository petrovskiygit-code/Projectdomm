from typing import AnyStr

import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state1(transactions: list) -> None:
    assert filter_by_state(transactions, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(transactions) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state2(transactions: list) -> None:
    assert filter_by_state(transactions, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state3(transactions: list) -> None:
    assert len(filter_by_state(transactions, "CANCELE")) == 0


def test_sort_by_date1(transactions: list) -> None:
    assert sort_by_date(transactions) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]


def test_sort_by_date2(transactions: list) -> None:
    assert sort_by_date(transactions, False) == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]


@pytest.mark.parametrize(
    "zed,result",
    [([{"id": 594226727, "state": "CANCELED"}], [])],
)
def test_sort_by_date3(zed: list, result: list) -> None:
    assert sort_by_date(zed) == result


@pytest.mark.parametrize(
    "zed,result",
    [([{"id": 594226727}], [])],
)
def test_filter_by_state5(zed: list, result: list) -> None:
    assert filter_by_state(zed) == result
