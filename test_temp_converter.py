import unittest
from temp_converter import *
class TempConverterTest(unittest.TestCase):
    # given temperature in celcius = correct value in F

    def test_celcius_is_converted_to_farenheit(self):
        """
            F = C * 9/5 + 32
        """
        actual = convert_celcius_to_farenheit(10)
        expected = 50
        self.assertEqual(actual,expected,"celcius should convert to correct Farenheit value")
