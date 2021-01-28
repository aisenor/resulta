# test output

import pytest
import runpy
import pathlib

import run # module
# from run import accept_input #function


# test dates from given example
# start_date = '2020-01-12'
# end_date = '2020-01-19'

def test_accept_input():
    run.input = lambda x: '2020-01-12'
    output_x = run.accept_input('start date')
    assert output_x == '2020-01-12'

    run.input = lambda y: '2020-01-19'
    output_y = run.accept_input('end date')
    assert output_y == '2020-01-19'

def test_team_rank(capfd):
    run.input = lambda y: '2020-01-19'
    output = run.main()
    out, err = capfd.readouterr()
    assert "event_id" in out
    assert "home_rank_points" in out
