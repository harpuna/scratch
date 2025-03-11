from services.jsonplaceholder import calculate_term_and_rate
from utils.calculator import calculate_monthly_payment


def test_calculate_monthly_payment():
    assert int(calculate_monthly_payment(1000000, (20 / 100.0), 24)) == 60000
    assert int(calculate_monthly_payment(1000000, (10 / 100.0), 36)) == 36972
    # TODO: add more cases...


def test_calculate_term_and_rate():
    assert calculate_term_and_rate(900000, 5) == (None, None)
    assert calculate_term_and_rate(5100000, 5) == (None, None)
    assert calculate_term_and_rate(1000000, 5) == (36, 10)
    assert calculate_term_and_rate(1000000, 20) == (24, 20)
    assert calculate_term_and_rate(1000000, 51) == (None, None)
    # TODO: add more cases...
