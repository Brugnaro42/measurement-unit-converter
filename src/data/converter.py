""" """
from lib2to3.pytree import convert
import sys


sys.path.append("../../src")
sys.path.append("../src")
sys.path.append("src")

sys.path.append("../../src/data")
sys.path.append("../src/data")
sys.path.append("src/data")


import conversion_metrics as cm
from utils.utils import initiate_log
from data.utils import get_currency_quotes

initiate_log()

class metrics_converter():

    def __init__(self):
        # TODO: Avaliar com o pessoal do front quais as unidades de medida que o pessoal utiliza
        self.round_flag = False
        self.weight_values = cm.weights
        self.area_values = cm.area
        self.length_values = cm.length
        self.currency_values = cm.currencies
    
    def __rule_of_three__(self, input_value: float, output_value: float, value_2b_converted: float, round_flag: bool = False)->float:
        """Apply the rule of three to easily convert the measure unities. 
           The principle is: input_num is to output_num as num_to_convert is to the function output, so: 
            'converted_value = (output_value/input_value) * value_2b_converted'

        Parameters
        ----------
        input_value : float
            The input used as param to calculate the conversion coefficient
        output_value : float
            The output used as param to calculate the conversion coefficient
        value_2b_convert : float
            The factor to be multiplied by the coefficient to get the function product
        round_flag : bool
            A flag to sinalize if the product will be rounded or not, by default False

        Returns
        -------
        float
            Product of the convertion
        """        
        # Calculate the coefficient
        coeff = output_value/input_value

        # Multiply by the value to be converted
        result = coeff * value_2b_converted

        # Return the product
        if round_flag:
            result = round(result, 3)
        
        return result

    def convert_weights(self, value_2b_converted: float, metric_input: str, metric_output: str, round_flag: bool=False)->float:
        """ Converts weight measurements following using the parameters 

        Parameters
        ----------
        value_2b_converted : float
            The weight to be converted is measured in the metric input and must be transferred to the metric output scale 
        metric_input : str
            The metric used as is:
            "bushel", "kg", "ton", "sc", "lb"
        metric_output : str
            The metric use to be:
           "bushel", "kg", "ton", "sc", "lb"
        product_name : str
            "Trigo", "Soja", "Milho", "Cevada", "Aveia"

        Returns
        -------
        float
            Returns the converted weight value
        """        

        # Test to check if the metrics are included in our dictionary
        weight_metrics = list(self.weight_values['All'].keys())

        assert metric_input in weight_metrics, f"Problem with the input metric {metric_input}"
        assert metric_output in weight_metrics, f"Problem with the output metric {metric_output}"

        origin = self.weight_values["All"][metric_input]
        destiny = self.weight_values["All"][metric_output]

        result = self.__rule_of_three__(origin, destiny, value_2b_converted, round_flag)

        return result
    
    def convert_temperature(self, value_2b_converted: float, metric_input: str, metric_output: str, round_flag: bool=False)->dict:
        """ Convert temperatures from celsius to fahrenheit /f to c

        Parameters
        ----------
        value_2b_converted : float
            The temperature to be converted is measured in the metric input and must be transferred to the metric output scale 
        metric_input : str
            The metric used as is:
            "f", "c"
        metric_output : str
            The metric use to be:
            "f", "c"

        Returns
        -------
        dict
           Returns the converted temperature value
        """        
        metric_input = metric_input.lower()
        metric_output = metric_output.lower()

        temperature_metrics = ['c','f']
        assert metric_input in temperature_metrics, f"Problem with the input metric {metric_input}"
        assert metric_output in temperature_metrics, f"Problem with the output metric {metric_output}"
        result = 0
        if metric_input == 'c':
            result = (value_2b_converted) * 9/5 + 32 
        elif metric_input == 'f':
            result = (value_2b_converted - 32 ) * 5/9 

        if round_flag:
            result = round(result, 3)

        return result
    
    def convert_area(self, value_2b_converted: float, metric_input: str, metric_output: str, round_flag: bool=False)->float:
        """ Converts area measurements

        Parameters
        ----------
        value_2b_converted : float
            The area to be converted is measured in the metric input and must be transferred to the metric output scale 
        metric_input : str
            The metric used as is:
            "ha", "ac"
        metric_output : str
            The metric use to be:
            "ha", "ac"

        Returns
        -------
        float
            Returns the converted area value
        """        
    
        # Test to check if the metrics are included in our dictionary
        area_metrics = list(self.area_values.keys())
        assert metric_input in area_metrics, f"Problem with the input metric {metric_input}"
        assert metric_output in area_metrics, f"Problem with the output metric {metric_output}"
        
        # Calculate the coeff for the conversion
        origin = self.area_values[metric_input]
        destiny = self.area_values[metric_output]

        # Make the conversion
        result = self.__rule_of_three__(origin, destiny, value_2b_converted, round_flag)

        return result
    
    def convert_lenght(self, value_2b_converted: float, metric_input: str, metric_output: str, round_flag: bool=False)->float:
        """ Converts length measurements

        Parameters
        ----------
        value_2b_converted : float
            The lenght to be converted is measured in the metric input and must be transferred to the metric output scale 
        metric_input : str
            The metric used as is:
            "in", "cm", "mm"
        metric_output : str
            The metric use to be:
           "in", "cm", "mm"

        Returns
        -------
        float
           Returns the converted lenght value
        """        
        
        # Test to check if the metrics are included in our dictionary
        lenght_metrics = list(self.length_values.keys())
        assert metric_input in lenght_metrics, f"Problem with the input metric {metric_input}"
        assert metric_output in lenght_metrics, f"Problem with the output metric {metric_output}"
        
        # Calculate the coeff for the conversion
        origin = self.length_values[metric_input]
        destiny = self.length_values[metric_output]

        # Make the conversion
        result = self.__rule_of_three__(origin, destiny, value_2b_converted, round_flag)

        return result

    def convert_currency(self, value_2b_converted: float, currency_input: str = "USD", currency_output: str = "BRL", round_flag: bool=False)->float:
        """ Convert currency value from USD to BRL

        Parameters
        ----------
        value_2b_converted : float
            The currency to be converted is measured in the metric input and must be transferred to the metric output scale 
        currency_input : str, optional
            The metric used as is:
            You can check the currencies in conversion_metrics, by default "USD"
        currency_output : str, optional
            The metric use to be:
            You can check the currencies in conversion_metrics, by default "BRL"

        Returns
        -------
        float
            Returns the converted currency value
        """        

        # Get the currency quotes to create a coefficient
        dict_convertion = get_currency_quotes(currency_in = currency_input, currency_out = currency_output)
        key = currency_input + currency_output
        coeff = dict_convertion[key]['ask']
        
        # Transform the value
        result = self.__rule_of_three__(1, coeff, value_2b_converted, round_flag)

        return result