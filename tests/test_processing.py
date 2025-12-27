from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(tronic, state_CANCELED, state_EXECUTED):
    assert filter_by_state(tronic, state="executed") == state_EXECUTED
    assert filter_by_state(tronic, state="canceled") == state_CANCELED


def test_sort_by_date(tronic, tronic_false):
    assert sort_by_date(tronic, date=True) == tronic
    assert sort_by_date(tronic, date=False) == tronic_false