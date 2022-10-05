"""
input one 'case' which some values need to be replaced

input case, variables, values
output updated_case
"""
import json
import re

from pytest_api.utils.config_handler import conf, EnvData
from pytest_api.utils.random_phone_number_generator import get_new_phone_number
from pytest_api.utils.random_string_generator import get_new_name, get_random_string


def replace_case_with_regular(case):
    """
    case is dict from excel-file.
    :param case:
    :return: replaced case
    """
    # transfer 'case' into string
    case_str = json.dumps(case)
    # replace_with_regular
    new_case = replace_with_regular(case_str)
    # transfer back to json dict, and return
    case_dict = json.loads(new_case)
    return case_dict


def replace_with_regular(data):
    """
    where are values from?
    1. EnvData class
    2. Config -conf.ini
    :param data: data
    :return: replaced data
    """
    res = re.findall("#(.*?)#", data)

    if res:
        for item in res:
            try:
                value = conf.get("data", item)
            except:
                # if no value currently, pass it
                try:
                    value = getattr(EnvData, item)
                except AttributeError:
                    value = f"#{item}#"
                    continue
            data = data.replace(f"#{item}#", value)
    return data


def replace_mark_with_value(case, mark, value):
    """
    replace marks with given value,
    :param case: case with key=value...
    :param mark: #XX#, #phone#, #url#
    :param value: expected value
    :return: new_case
    """
    for k, v in case.items():
        # string operation only, so pass all non-string and None
        if v is not None and isinstance(v, str):
            # if mark exist, replace
            if v.find(mark) != -1:
                case[k] = v.replace(mark, value)

    return case


if __name__ == '__main__':
    case_example = {"id": 1, "data": "a#phone#", "url": "http://#url#/", "expected": "#phone#"}
    print(replace_mark_with_value(case_example, "#phone#", "12345678"))
    print(replace_mark_with_value(case_example, "#url#", "alex-info.ca"))

    setattr(EnvData, "username", get_new_name())
    setattr(EnvData, "phone", get_new_phone_number())
    setattr(EnvData, "password", get_random_string(8))
    data_example = '{"username":"#username#","mobile":"#phone#","password":"#password#","email":"a@a.com"}'
    print(replace_with_regular(data_example))


