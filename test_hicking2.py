"""Test hicking.py"""

import os
import sys
import subprocess
import pytest

base_param = [os.path.join(os.path.dirname(__file__), "hicking2.py")]
if sys.platform == "win32":
    base_param = ["python"] + base_param


DATA_IN = [os.path.join(os.getcwd(), ".test", f"{i:0>2}.in") for i in range(1, 12)]

DATA_OUT = [
    "1",
    "2",
    "3",
    "6",
    "13",
    "5",
    "9",
    "16",
    "35",
    "82",
    "1162",
]


@pytest.mark.parametrize(
    "input_data, expected_output",
    zip(DATA_IN, DATA_OUT),
)
def test_hicking_single(input_data, expected_output):
    """Test hicking.py"""
    param = ["python"] + base_param + [input_data]
    result = subprocess.run(
        param,
        input=input_data[1],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.stdout == f"{expected_output}\n"
