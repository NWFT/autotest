
"""
Following some rules, (3+8, 4+7)
generate a random mobile phone number.

"""
from random import randint

from api.utils.db_mysql_handler import handle_db

"""
Alberta(1)587
British Columbia(1)250
British Columbia(1)604
British Columbia(1)778
Greater Toronto Area(1)289
Greater Toronto Area(1)905
Manitoba(1)204
Montreal(1)514
New Brunswick(1)506
Newfoundland(1)709
Ontario(1)226
Ontario(1)519
Ontario(1)613
Ontario(1)705
Ontario(1)807
Quebec(1)819
Saskatchewan(1)306
"""
"""
China Mobile: 134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 178, 182, 183, 184, 187, 188, 198
China Telecom: 133, 153, 173, 177, 180, 181, 189, 191, 199
China Unicom: 130, 131, 132, 155, 156, 166, 167, 171, 176, 185, 186
"""
prefix_cn = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 178, 182, 183, 184, 187, 188, 198,
             133, 153, 173, 177, 180, 181, 189, 191, 199,
             130, 131, 132, 155, 156, 166, 167, 171, 176, 185, 186]


def get_new_phone_number():
    while True:
        num = __phone_number_generator()
        if not __check_number(num):
            break
    # handle_db.close_connections()
    return num


def __phone_number_generator():
    random_index = randint(0, len(prefix_cn) - 1)
    phone = str(prefix_cn[random_index])
    for _ in range(8):
        phone += str(randint(0, 9))

    return phone


def __check_number(num):
    sql = f"select * from tb_users WHERE mobile='{num}'"
    count = handle_db.get_count(sql)
    return count


if __name__ == '__main__':
    print(get_new_phone_number())
