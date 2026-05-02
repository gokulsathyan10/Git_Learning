import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.python import add, subtract, multiply, divide

def test_operations():
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    assert multiply(2, 3) == 6
    assert divide(6, 2) == 3

if __name__ == "__main__":
    test_operations()