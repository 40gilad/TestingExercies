import source.shapes as shapes
import math
import pytest


def test_area(rec):
    desired_result = 28

    actual_result = round(rec.area(), 3)
    print(actual_result)
    assert desired_result == actual_result


def test_perimeter(rec):
    desired_result = 22

    actual_result = round(rec.perimeter(), 3)

    assert desired_result == actual_result


def test_eq(rec, second_rec):
    desired_result = False

    actual_result = rec == second_rec

    assert desired_result == actual_result
