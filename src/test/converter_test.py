""" Test suits to test the convert functions"""
import logging
import sys

sys.path.append("../../src")
sys.path.append("../src")
sys.path.append("src")

sys.path.append("../../src/data")
sys.path.append("../src/data")
sys.path.append("src/data")

from utils.utils import *
from data.utils import get_currency_quotes
from data.converter import metrics_converter


initiate_log()

converter = metrics_converter()

# WEIGHT CONVERSIONS
def test_convert_weights_kg_ton():
    '''Convert tests :: weight converts :: Should test the convertion kg->ton'''
    # Input params
    input_metric = "kg"
    output_metric = "ton"
    value = 1000

    # Executing tests
    logging.info(f"Testing weight convertion for {input_metric}->{output_metric}")
    result = converter.convert_weights(value, input_metric, output_metric)

    # Making the compares
    expect = 1
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}->{output_metric}, expected: {expect}, got {result}""" 

def test_convert_weights_sc_kg():
    '''Convert tests :: weight converts :: Should test the convertion Corn Bushel->kg'''
    # Input params
    input_metric = "sc"
    output_metric = "kg"
    value = 1000

    # Executing tests
    logging.info(f"Testing weight convertion for {input_metric}->{output_metric}")
    result = converter.convert_weights(value, input_metric, output_metric, True)

    # Making the compares
    expect = 60000
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}->{output_metric}, expected: {expect}, got {result}"""

def test_convert_weights_sc_ton():
    '''Convert tests :: weight converts :: Should test the convertion Corn Bushel->kg'''
    # Input params
    input_metric = "sc"
    output_metric = "ton"
    value = 1000

    # Executing tests
    logging.info(f"Testing weight convertion for {input_metric}->{output_metric}")
    result = converter.convert_weights(value, input_metric, output_metric, True)

    # Making the compares
    expect = 60
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}->{output_metric}, expected: {expect}, got {result}"""

# AREA CONVERSIONS
def test_convert_area_ha_ac():
    '''Convert tests :: area converts :: Should test the convertion ha->ac'''
    # Input params
    input_metric = "ha"
    output_metric = "ac"
    value = 1000

    # Executing tests
    logging.info(f"Testing area convertion for {input_metric}->{output_metric}")
    result = converter.convert_area(value, input_metric, output_metric)
    
    # Making the compares
    expect = 2471
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}{output_metric}, 
        expected: {expect}, got {result}""" 

def test_convert_area_ac_ha():
    '''Convert tests :: area converts :: Should test the convertion Corn ac->ha'''
    # Input params
    input_metric = "ac"
    output_metric = "ha"
    value = 24.71

    # Executing tests
    logging.info(f"Testing area convertion for {input_metric}->{output_metric}")
    result = converter.convert_area(value, input_metric, output_metric)

    # Making the compares
    expect = 10
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}{output_metric}, 
        expected: {expect}, got {result}""" 

# LENGHT CONVERSIONS
def test_convert_lenght_cm_mm():
    '''Convert tests :: lenght converts :: Should test the convertion cm->mm'''
    # Input params
    input_metric = "cm"
    output_metric = "mm"
    value = 1

    # Executing tests
    logging.info(f"Testing lenght convertion for {input_metric}->{output_metric}")
    result = converter.convert_lenght(value, input_metric, output_metric)

    # Making the compares
    expect = 10
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}{output_metric}, 
        expected: {expect}, got {result}""" 

def test_convert_lenght_in_cm():
    '''Convert tests :: lenght converts :: Should test the convertion in->cm'''
    # Input params
    input_metric = "in"
    output_metric = "cm"
    value = 1

    # Executing tests
    logging.info(f"Testing lenght convertion for {input_metric}->{output_metric}")
    result = converter.convert_lenght(value, input_metric, output_metric, True)

    # Making the compares
    expect = 2.54
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}->{output_metric}, expected: {expect}, got {result}""" 

# TEMPERATURE CONVERSIONS
def test_convert_temperature_c_f():
    '''Convert tests :: temperature converts :: Should test the convertion C°->F°'''
    # Input params
    input_metric = "c"
    output_metric = "f"
    value = 10

    # Executing tests
    logging.info(f"Testing temperature convertion for {input_metric}->{output_metric}")
    result = converter.convert_temperature(value, input_metric, output_metric)

    # Making the compares
    expect = 50
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}{output_metric}, 
        expected: {expect}, got {result}"""

def test_convert_temperature_f_c():
    '''Convert tests :: temperature converts :: Should test the convertion F°->C°'''

    # Input params
    input_metric = "f"
    output_metric = "c"
    value = 32

    # Executing tests
    logging.info(f"Testing temperature convertion for {input_metric}->{output_metric}")
    result = converter.convert_temperature(value, input_metric, output_metric)

    # Making the compares
    expect = 0
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_metric}{output_metric}, 
        expected: {expect}, got {result}"""

# CURRENCY CONVERSIONS
def test_convert_currency_usd_brl():
    '''Convert tests :: currency converts :: Should test the convertion USD->BRL'''

    # Input params
    input_currency = "USD"
    output_currency = "BRL"
    value = 1

    # Executing tests
    logging.info(f"Testing currency convertion for {input_currency}->{output_currency}")
    result = converter.convert_currency(value, input_currency, output_currency, True)

    # Making the compares
    expect = get_currency_quotes(input_currency, output_currency)
    key = f"{input_currency}{output_currency}"
    expect = expect[key]["ask"]
    expect = round(expect, 3)
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_currency}{output_currency}, 
        expected: {expect}, got {result}"""

def test_convert_currency_eur_brl():
    '''Convert tests :: currency converts :: Should test the convertion EUR->BRL'''
    # Input params
    input_currency = "EUR"
    output_currency = "BRL"
    value = 1

    # Executing tests
    logging.info(f"Testing currency convertion for {input_currency}->{output_currency}")
    result = converter.convert_currency(value, input_currency, output_currency)

    # Making the compares
    expect = get_currency_quotes(input_currency, output_currency)
    key = f"{input_currency}{output_currency}"
    expect = expect[key]["ask"]
    expect = round(expect, 3)
    assert result == expect, \
        f"""Output value unexpected, check this conversion: {input_currency}{output_currency}, expected: {expect}, got {result}"""
    