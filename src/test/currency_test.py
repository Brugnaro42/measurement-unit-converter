""" Test suits to the currency functions"""
import logging
from operator import mod
import sys

sys.path.append("../../src")
sys.path.append("../src")
sys.path.append("src")
sys.path.append("../../src/data")
sys.path.append("../src/data")
sys.path.append("src/data")

from utils.utils import *
from data.utils import *

initiate_log()

# Test these features
#   [x] - get currency

def test_get_currency():
    result = get_currency_quotes()
    logging.info(result)
    expect = 5.1061

    diff = expect - result['USDBRL']['ask']
    diff = (diff **2)**0.5
    
    assert diff < 0.1, f"Problem with the results, check the inputs. Expected {expect} Got {result['USDBRL']['ask']}"
    logging.info("Sucessfull test for test_get_currency")