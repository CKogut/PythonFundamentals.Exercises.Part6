from typing import Iterable, Tuple


def convert_to_celsius(input_temp: float, input_unit_of_measurement: str)-> float:
    """
    Given a float representing a temperature in fahrenheit or kelvin, return the corresponding value in celsius.

    :param input_temp: A float representing a temperature in fahrenheit or kelvin
    :return: A float representing the corresponding value of the input_temp parameter in celsius
    """
    if input_unit_of_measurement == 'f':
        celsius = (input_temp - 32) * 5 / 9
        return round(celsius, 2)
    elif input_unit_of_measurement == 'k':
        celsius = input_temp - 273.15
        return round(celsius, 2)
    else:
        print('Invalid input')


def convert_to_fahrenheit(input_temp: float, input_unit_of_measurement: str) -> int:
    """
    Given a float representing a temperature in celsius or kelvin, return the corresponding value in fahrenheit.

    :param input_temp: A float representing a temperature in celsius or kelvin
    :return:  A float representing the corresponding value of the input_temp parameter in fahrenheit
    """
    if input_unit_of_measurement == 'c':
        fahrenheit = (input_temp * 9 / 5) + 32
        return int(fahrenheit)
    elif input_unit_of_measurement == 'k':
        fahrenheit = (input_temp - 273.15) * (9/5) + 32
        return int(fahrenheit)
    else:
        print('Invalid input')


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str, output_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """

    # Create two lists
    orig_temp = []
    converted = []

    # Loop through tuple and assign value to orig_temp
    for i in temperatures:
        orig_temp.append(i)
        # Bases on input_of_measurement, convert and assign to converted
        if input_unit_of_measurement == 'c':
            converted.append(convert_to_fahrenheit(i, output_unit_of_measurement))
        elif input_unit_of_measurement == 'f':
            converted.append(convert_to_celsius(i, output_unit_of_measurement))
        else:
            pass

    # Zip the two together
    return tuple(zip(orig_temp, converted))

