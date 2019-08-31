import pytest
from solution import solution


@pytest.mark.parametrize(('input', 'expected'), [
    (1, 1),
    ])
def test_walk(input, expected):
    assert solution(input) == expected
