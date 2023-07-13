import pytest
import time
import random

def test_():
    a = 1
    b = random.randint(1, 2)    // 50% chance of failure

    time.sleep(20)
    time.sleep(20)

    assert a != b
