import requests
import json
import os

class APIClient:
    requestSampleString = ""
    hasArrayInJson = False
    hasStringOnlyJson = False
    hasIntOnlyJson = False

def get_object_type_name(obj):
    return type(obj).__name__

def get_dictionary_based_on_input_json_type(input_obj):
    dictionary_obj = {}
    obj_type = get_object_type_name(input_obj)

    if obj_type == 'list':
        global hasArrayInJson
        hasArrayInJson = True
        for index, item in enumerate(input_obj):
            item_type = get_object_type_name(item).lower()

            if 'dict' in item_type:
                if len(input_obj) == 1:
                    dictionary_obj = input_obj[0]
                else:
                    dictionary_obj[f'[{index}]'] = item

            elif 'str' in item_type:
                key = 'proxyKey' if len(input_obj) == 1 else f'[{index}].proxyKey'
                dictionary_obj[key] = item

            elif 'int' in item_type or 'float' in item_type:
                value_to_add = int(item)
                key = 'proxyIntKey' if len(input_obj) == 1 else f'[{index}].proxyIntKey'
                dictionary_obj[key] = value_to_add

    elif 'dict' in obj_type.lower():
        dictionary_obj = input_obj

    elif 'str' in obj_type.lower():
        global hasStringOnlyJson
        hasStringOnlyJson = True
        if ',' in input_obj:
            split_strings = input_obj.split(',')
            for index, val in enumerate(split_strings):
                dictionary_obj[f'[{index}].proxyKey'] = val
        else:
            dictionary_obj['proxyKey'] = input_obj

    elif 'int' in obj_type.lower() or 'float' in obj_type.lower():
        global hasIntOnlyJson
        hasIntOnlyJson = True
        input_str = str(input_obj)
        if ',' in input_str:
            split_ints = input_str.split(',')
            for index, val in enumerate(split_ints):
                value_to_add = int(val)
                dictionary_obj[f'[{index}].proxyIntKey'] = value_to_add
        else:
            dictionary_obj['proxyIntKey'] = int(input_obj)

    return dictionary_obj
