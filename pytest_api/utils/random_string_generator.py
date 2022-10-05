import random
import string

from pytest_api.utils.db_mysql_handler import handle_db


def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


def get_new_name():
    while True:
        tmp_str = get_random_string(10)
        sql = f"select * from tb_users WHERE username='{tmp_str}'"
        if not handle_db.get_count(sql):
            break
    return tmp_str


if __name__ == '__main__':
    for _ in range(2):
        print(get_random_string(10))

    print(get_new_name())
