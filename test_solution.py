import pytest
from solution import solution


@pytest.mark.parametrize(('input', 'expected'), [
    (1, 1),
    ])
def test_solution(input, expected):
    assert solution(input) == expected
