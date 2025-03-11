import pytest
import source.shapes as shapes


@pytest.mark.parametrize("length, expected_area", [(4, 16), (8, 64), (10, 100)])
def test_multiple_square_areas(length, expected_area):
    desired_result = expected_area

    actual_result = shapes.Square(length).area()

    assert desired_result == actual_result


perimeters_list = [(3, 12), (4, 16), (5, 20)]


@pytest.mark.parametrize("length, expected_perimeter", perimeters_list)
def test_multiple_square_perimeters(length, expected_perimeter):
    desired_result = expected_perimeter

    actual_result = shapes.Square(length).perimeter()

    assert desired_result == actual_result
