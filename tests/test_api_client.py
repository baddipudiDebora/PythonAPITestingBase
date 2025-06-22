import unittest
import json
import os

from utils.api_client import get_dictionary_based_on_input_json_type


class TestGetDictionaryBasedOnInputJsonType(unittest.TestCase):

    def test_dict_input(self):
        data = {"name": "Debora", "city": "Brampton"}
        result = get_dictionary_based_on_input_json_type(data)
        self.assertEqual(result, data)

    def test_list_single_string(self):
        data = ["hello"]
        result = get_dictionary_based_on_input_json_type(data)
        self.assertEqual(result, {"proxyKey": "hello"})

    def test_list_multiple_strings(self):
        data = ["apple", "banana"]
        result = get_dictionary_based_on_input_json_type(data)
        expected = {
            "[0].proxyKey": "apple",
            "[1].proxyKey": "banana"
        }
        self.assertEqual(result, expected)

    def test_list_of_integers(self):
        data = [10, 20]
        result = get_dictionary_based_on_input_json_type(data)
        expected = {
            "[0].proxyIntKey": 10,
            "[1].proxyIntKey": 20
        }
        self.assertEqual(result, expected)

    def test_list_of_dicts(self):
        data = [{"id": 1}, {"id": 2}]
        result = get_dictionary_based_on_input_json_type(data)
        expected = {
            "[0]": {"id": 1},
            "[1]": {"id": 2}
        }
        self.assertEqual(result, expected)

    def test_single_integer(self):
        data = 42
        result = get_dictionary_based_on_input_json_type(data)
        self.assertEqual(result, {"proxyIntKey": 42})

    def test_comma_separated_string(self):
        data = "red,green,blue"
        result = get_dictionary_based_on_input_json_type(data)
        expected = {
            "[0].proxyKey": "red",
            "[1].proxyKey": "green",
            "[2].proxyKey": "blue"
        }
        self.assertEqual(result, expected)

    def test_comma_separated_number_string(self):
        data = ["100","200"]
        result = get_dictionary_based_on_input_json_type(data)
        expected = {
            "[0].proxyKey": "100",
            "[1].proxyKey": "200"
        }
        self.assertEqual(result, expected)

    def test_float_input(self):
        data = 3.14
        result = get_dictionary_based_on_input_json_type(data)
        self.assertEqual(result, {"proxyIntKey": 3})

    def test_flat_json_user_profile(self):
        # This mimics your uploaded single_object.json
        data = {
            "id": 109,
            "username": "DebXYZ",
            "firstName": "AutoTest",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": 0
        }
        result = get_dictionary_based_on_input_json_type(data)
        self.assertIsInstance(result, dict)
        self.assertEqual(result.get("username"), "DebXYZ")
        self.assertEqual(result.get("id"), 109)

if __name__ == "__main__":
    unittest.main()