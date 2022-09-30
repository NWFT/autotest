"""
input one 'case' which some values need to be replaced

input case, variables, values
output updated_case
"""


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
