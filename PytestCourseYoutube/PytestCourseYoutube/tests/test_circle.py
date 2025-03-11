import source.shapes as shapes
import math


class TestCircle:
    def setup_method(self, method):
        print(f"\nSETUP: {method.__name__}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"TEARDOWN: {method.__name__}")
        del self.circle

    def test_area(self):
        desired_result = 314.159

        actual_result = round(self.circle.area(), 3)
        print(actual_result)
        assert desired_result == actual_result

    def test_perimeter(self):
        desired_result = 62.832

        actual_result = round(self.circle.perimeter(), 3)

        assert desired_result == actual_result

    def test_not_same_shape_eq(self,rec):
        desired_result = False

        actual_result = rec == self

        assert actual_result == desired_result
