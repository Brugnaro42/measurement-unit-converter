""" Utils class to Extract, Transform and Load data"""
import requests
import logging
import json
import sys

sys.path.append("../../src/data")
sys.path.append("../../src")
sys.path.append("../src")
sys.path.append("src")

import conversion_metrics as cm

from utils.utils import *

initiate_log()


def get_currency_quotes(currency_in: str = "USD", currency_out: str = "BRL", api_url: str = 'https://economia.awesomeapi.com.br/json/daily/', )->dict:
    """Returns the currency quotes values
    You can check the currencies in conversion_metrics.py file,

    Parameters
    ----------
    api_url : _type_, optional
        URL to be requested to get the curency quote, by default 'https://economia.awesomeapi.com.br/json/daily/'
    currency_in : str, optional
        The currency used as is, by default "USD"
    currency_out : str, optional
        The currency as to be, by default "BRL"

    Returns
    -------
    dict
        Returns the value of the currency of the day
    """    
    # Make the asserts
    currencies = list(cm.currencies.keys())
    assert currency_in in currencies, f"Problem with the input currency {currency_in}"
    assert currency_out in currencies, f"Problem with the output currency {currency_out}"

    # Treat the Dolar cents exception
    exception_cent_flag_in, exception_cent_flag_out = False, False
    if currency_in == 'c':
        currency_in = 'USD'
        exception_cent_flag_in = True
    
    if currency_out == 'c':
        currency_out = 'USD'
        exception_cent_flag_out = True

    # Make the HTTP GET Request:
    url_2b_requested = f"{api_url}{currency_in}-{currency_out}/2" # We have a '2' in order to get the yesterday price
    logging.info(f"Requesting from {url_2b_requested}")
    request = requests.get(url_2b_requested)
    assert request.status_code == 200, f"Status-code: {request.status_code}, Something went wrong requesting this URL: {url_2b_requested} "

    # Convert the results in a dictionary
    content = request.content
    result = json.loads(content)       
 
    result = result[1]
    key = f"{currency_in}{currency_out}"
    result[key] = result
    result[key]['ask'] = float(result['ask'])
    logging.info(f"Got the values for {currency_in}{currency_out} with success")

    # Treat the Dolar cents exception back convertion
    if exception_cent_flag_in or exception_cent_flag_out:
        if exception_cent_flag_in:
            result[key]['ask'] = result[key]['ask'] / 100
            currency_in='C'
            new_key = f"{currency_in}{currency_out}"

        if exception_cent_flag_out:
            result[key]['ask'] = result[key]['ask'] * 100
            currency_out='C'

        new_key = f"{currency_in}{currency_out}"
        result[new_key] = result[key]
        result.pop(key)
    
    return result