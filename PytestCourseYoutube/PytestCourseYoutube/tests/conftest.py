import pytest
import source.shapes as shapes


@pytest.fixture
def rec():
    return shapes.Rectangle(7, 4)


@pytest.fixture
def second_rec():
    return shapes.Rectangle(5, 6)
