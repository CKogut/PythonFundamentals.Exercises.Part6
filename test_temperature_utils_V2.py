import unittest
import temperature_utils_V2


class TemperatureUtilsTest(unittest.TestCase):

    def test_convert_fahrenheit_to_celsius(self):
        test_cases = [
            (32, 0),
            (68, 20),
            (100, 37.78),
            (104, 40)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_V2.convert_to_celsius(temp_in, 'f'))

    def test_convert_kelvin_to_celsius(self):
        test_cases = [
            (0, -273.15),
            (30, -243.15),
            (60, -213.15),
            (100, -173.15)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_V2.convert_to_celsius(temp_in, 'k'))

    def test_convert_invalid_to_celsius(self):
        test_cases = [
            (0, None),
            (30, None),
            (60, None),
            (100, None)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_V2.convert_to_celsius(temp_in, 'b'))

    def test_convert_celsius_to_fahrenheit(self):
        test_cases = [
            (-17.7778, 0),
            (0, 32),
            (100, 212)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_V2.convert_to_fahrenheit(temp_in, 'c'))

    def test_convert_kelvin_to_fahrenheit(self):
        test_cases = [
            (0, -459),
            (300, 80),
            (350, 170)
        ]
        for temp_in, expected in test_cases:
            with self.subTest(f"{temp_in} -> {expected}"):
                self.assertEqual(expected, temperature_utils_V2.convert_to_fahrenheit(temp_in, 'k'))

    def test_temperature_tuple(self):
        temps_input = (32, 68, 100, 104)
        expected = ((32, 0.0), (68, 20.0), (100, 37.78), (104, 40.0))
        actual = temperature_utils_V2.temperature_tuple(temps_input, "f", "c")
        self.assertEqual(expected, actual)

    def test2_temperature_tuple(self):
        temps_input = (-17.7778, 0, 100)
        expected = ((-17.7778, 0.0), (0, 32.0), (100, 212.0))
        actual = temperature_utils_V2.temperature_tuple(temps_input, "c", "f")
        self.assertEqual(expected, actual)

    def test3_temperature_tuple(self):
        temps_input = (0, 300, 350)
        expected = ((0, -459), (300, 80), (350, 170))
        actual = temperature_utils_V2.temperature_tuple(temps_input, "k", "f")
        self.assertEqual(expected, actual)

    def test4_temperature_tuple(self):
        temps_input = (0, 30, 60)
        expected = ((0, -273.15), (30, -243.15), (60, -213.15))
        actual = temperature_utils_V2.temperature_tuple(temps_input, "k", "c")
        self.assertEqual(expected, actual)

    def test5_temperature_tuple(self):
        temps_input = (1, 2, 3)
        self.assertEqual(tuple(), temperature_utils_V2.temperature_tuple(temps_input, "a", "g"))

