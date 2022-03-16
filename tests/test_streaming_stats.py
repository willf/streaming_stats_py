import pytest

from streaming_stats.streaming_stats import stats
import math

__author__ = "Will Fitzgerald"
__copyright__ = "Will Fitzgerald"
__license__ = "MIT"



def test_stats():
    results = stats([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert results["n"] == 10
    assert results["mean"] == 5.5
    assert results["variance"] == 8.25
    assert results["stddev"] == math.sqrt(results["variance"])
    assert results["min"] == 1
    assert results["max"] == 10
    assert results["sum"] == 55

