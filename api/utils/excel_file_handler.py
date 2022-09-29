from openpyxl import load_workbook
import json


class HandleExcel:

    def __init__(self, file_dir, sheet_name):
        self.wb = load_workbook(file_dir)
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:
            # get every column's value in the first line in xls-file
            titles.append(item.value)
        return titles

    def read_all_data(self):
        all_data = []
        titles = self.__read_titles()
        # every line but the first one
        for item in list(self.sh.rows)[1:]:
            values = []
            # get every column's value
            for val in item:
                values.append(val.value)
            # zip to dict with titles
            res = dict(zip(titles, values))
            # transfer string into json format
            res["request_data"] = json.loads(res["request_data"])
            all_data.append(res)
        return all_data

    def close_file(self):
        self.wb.close()


if __name__ == '__main__':
    import os

    from api.utils.path_handler import data_dir

    file_path = os.path.join(data_dir, "api_test_cases_single.xlsx")
    exc = HandleExcel(file_path, "login")
    cases = exc.read_all_data()
    exc.close_file()
    for case in cases:
        print(case)
