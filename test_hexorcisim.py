import pytest
from hexorcisim import to_decimal, from_decimal

def decimal_covert():
    assert to_decimal("C7", 16) == 199

def to_targetconvert():
    assert from_decimal(199, 16) == "C7"
