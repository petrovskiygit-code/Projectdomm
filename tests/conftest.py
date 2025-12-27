import pytest

@pytest.fixture()
def tronic():
    return [
        {"id": 29282726, "state": "executed","date": "2024.19.01T20:20:30.512364"},
        {"id": 30313233, "state": "executed","date": "2020.03.04T21:12:35.349084"},
        {"id": 32333438, "state": "canceled","date": "2018.05.06T18:45:30.358902"},
        {"id": 34353334, "state": "canceled","date": "2016.06.06T20:45:10.345689"},
    ]



@pytest.fixture()
def state_CANCELED():
    return [
        {"id": 32333438, "state": "canceled", "date": "2018.05.06T18:45:30.358902"},
        {"id": 34353334, "state": "canceled", "date": "2016.06.06T20:45:10.345689"},
    ]



@pytest.fixture()
def state_EXECUTED():
    return [
        {"id": 29282726, "state": "executed", "date": "2024.19.01T20:20:30.512364"},
        {"id": 30313233, "state": "executed", "date": "2020.03.04T21:12:35.349084"},
    ]



@pytest.fixture()
def tronic_false():
    return [
        {"id": 34353334, "state": "canceled", "date": "2016.06.06T20:45:10.345689"},
        {"id": 32333438, "state": "canceled", "date": "2018.05.06T18:45:30.358902"},
        {"id": 30313233, "state": "executed", "date": "2020.03.04T21:12:35.349084"},
        {"id": 29282726, "state": "executed","date": "2024.19.01T20:20:30.512364"}
    ]



