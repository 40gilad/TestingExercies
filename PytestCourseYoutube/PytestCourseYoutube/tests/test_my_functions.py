import time

import pytest
import source.my_functions as mf


def test_add_function_should_return_sum_of_two_numbers():
    func = mf.add
    first_num, second_num = 3, 4
    required_result = 7

    result = func(first_num, second_num)
    assert result == required_result


def test_add_strings_should_return_first_concated_to_second():
    func = mf.add
    first, second = "Gilad Meir", " doing tests"
    required_result = "Gilad Meir doing tests"

    result = func(first, second)
    assert result == required_result


def test_divide_function_should_return_division_of_first_in_second():
    func = mf.divide
    first_num, second_num = 8, 4
    required_result = 2

    result = func(first_num, second_num)
    assert result == required_result


def test_divide_by_zero_should_raise_ZeroDivisionError():
    func = mf.divide
    first_num, second_num = 8, 0

    with pytest.raises(ValueError):
        func(first_num, second_num)


@pytest.mark.kaki
def test_very_slow():
    time.sleep(1)
    assert True


@pytest.mark.skip(reason="check the skip feature in pytest")
def test_skip_feature_of_pytest():
    assert False


@pytest.mark.xfail(reason = "checking the xfaile feature")
def test_xfaile_feature_of_pytest():
    func = mf.add
    first_num, second_num = 3, 4
    required_result = 8

    result = func(first_num, second_num)
    assert result == required_result
