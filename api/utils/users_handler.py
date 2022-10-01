def get_admin_user():
    """
    Read user fom conf.ini,
    if exist, return,
    if not, create and return
    :return:
    """
    from api.utils.config_handler import conf
    user = conf.get("admin_user", "username")
    passwd = conf.get("admin_user", "password")
    phone = conf.get("admin_user", "phone")

    return user, passwd, phone


def get_normal_user():
    pass
