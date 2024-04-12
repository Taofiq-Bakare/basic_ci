from calculator import add_


def test_can_add_two_floats():
    a = 1
    b = 2
    result = add_(a, b)
    assert result == 3
