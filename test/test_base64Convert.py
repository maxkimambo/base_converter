from unittest import TestCase
from converter.Base64Convert import Base64Convert

class TestBase64Convert(TestCase):

    def test_converter_should_convert_number_to_base64(self):
        conv = Base64Convert()
        result = conv.convert(999999999999999999)

        self.assertEqual('bl3aOWDLlUh', result)

    def test_converter_should_revert_back_to_number(self):
        conv = Base64Convert()
        result = conv.revert('bl3aOWDLlUh')
        self.assertEqual(999999999999999999, result)