# test output

import pytest
import runpy
import pathlib

import run # module
# from run import accept_input #function


# test dates from given example
# start_date = '2020-01-12'
# end_date = '2020-01-19'

def test_output():
    run.input = lambda x: '2020-01-12'
    output = run.accept_input('start date')
    assert output == '2020-01-12'

    run.input = lambda y: '2020-01-19'
    output = run.accept_input('end date')
    assert output == '2020-01-19'
    # output = run
    # runpy.run_path(script)
    # accept_input.input = lambda: '2020-01-01'
    # output = accept_input('start date')
    # assert output == '2020-01-01'
    assert 1==1
