# test output

import pytest

# hard coded for tests
start_date = '2020-01-12'
end_date = '2020-01-19'

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
