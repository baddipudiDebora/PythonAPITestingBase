import os
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

import pytest

from utils.helpers import get_object_type_name, get_full_file_path, read_file_from_path_and_get_file_content, \
    store_json_sample_string, write_to_file_from_path


class test_helpers(unittest.TestCase):

        def test_get_object_type_name_with_list(self):
            assert get_object_type_name([1, 2]) == "list"

        def test_get_object_type_name_with_dict(self):
            assert get_object_type_name({"name": "Debora"}) == "dict"

        def test_get_object_type_name_with_str(self):
            assert get_object_type_name("hello") == "str"

        def test_get_object_type_name_with_int(self):
            assert get_object_type_name(42) == "int"

        def test_get_object_type_name_with_float(self):
            assert get_object_type_name(3.14) == "float"

        def test_get_object_type_name_with_bool(self):
            assert get_object_type_name(True) == "bool"

        def test_get_object_type_name_with_none(self):
            assert get_object_type_name(None) == "NoneType"

        def test_get_object_type_name_with_tuple(self):
            assert get_object_type_name((1, 2)) == "tuple"

        def test_get_object_type_name_with_set(self):
            assert get_object_type_name({1, 2, 3}) == "set"

        def test_get_object_type_name_with_bytes(self):
            assert get_object_type_name(b"hello") == "bytes"


        # test for getting file full path
        def test_get_full_file_path_returns_expected_absolute_path(self):
                    folder_name = "data"
                    result = get_full_file_path(folder_name)
                    expected = os.path.abspath(
                        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", folder_name)
                    )
                    assert result == expected
                    assert os.path.isabs(result)

        from utils.helpers import read_file_from_path_and_get_file_content

        def test_read_file_from_path_and_get_file_content_success(self):
            with tempfile.TemporaryDirectory() as tmpdirname:
                    tmp_path = Path(tmpdirname)
                    # Create a test folder and file inside the temp directory
                    folder = tmp_path / "test_json_folder"
                    folder.mkdir()
                    file = folder / "sample.json"
                    content = '{"name": "Debora"}'
                    file.write_text(content, encoding="utf-8")
                    # Modify your function to accept full path instead of relying on __file__
                    file_path = file.resolve()
                    # You can test the content directly by mocking or adapting the function
                    result = read_file_from_path_and_get_file_content(
                        json_folder_name=folder.name,
                        file_name=file.name,
                        base_path=tmp_path
                    )
                    assert result == content

        def test_read_file_from_path_and_get_file_content_missing_file(self):
            with pytest.raises(Exception) as exc_info:
                read_file_from_path_and_get_file_content("nonexistent_folder", "missing.json",base_path=None)
            assert "Error reading JSON sample" in str(exc_info.value)

        def test_store_json_sample_string_success(self):
            with tempfile.TemporaryDirectory() as tmpdirname:
              tmp_path = Path(tmpdirname)
              folder = tmp_path / "mock_folder"
              folder.mkdir()
              file = folder / "mock.json"
              content = '{"greeting": "Hello, Debora!"}'
              file.write_text(content, encoding="utf-8")
              result = store_json_sample_string(
                json_folder_name=folder.name,
                file_name=file.name,
                base_path=tmp_path  # inject clean base path
            )
            self.assertEqual(result ,content)


        def test_store_json_sample_string_raises_for_empty(self):
            with tempfile.TemporaryDirectory() as tmpdirname:
                tmp_path = Path(tmpdirname)
                folder = tmp_path / "empty_folder"
                folder.mkdir()
                file = folder / "empty.json"
                file.write_text("", encoding="utf-8")

                with pytest.raises(ValueError, match="JSON sample string must not be null or empty"):
                    store_json_sample_string(
                        json_folder_name=folder.name,
                        file_name=file.name,
                        base_path=tmp_path
                    )

        def test_write_to_file_from_path(self):
            with tempfile.TemporaryDirectory() as tmpdirname:
                tmp_path = Path(tmpdirname)
                folder = tmp_path / "empty_folder"
                print(folder)
                folder.mkdir()
                file = folder / "empty.json"
                texttowrite = 'This data is writen by file write object and the time it is written is - '+str(datetime.now())
                write_to_file_from_path("empty_folder", "empty.json", texttowrite, base_path="F:/Python Practise")
                self.assertEqual(read_file_from_path_and_get_file_content("empty_folder", "empty.json", "F:/Python Practise"),texttowrite)

