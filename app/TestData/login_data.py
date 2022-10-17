
# login user
login_data = {"user": "aaaaaa", "password": "qqqqqqqq"}

# invalid login user
invalid_data = [
        {"user": "", "password": "qqqqqqqq", "check": "缺少用户名或密码"},
        {"user": "aaa", "password": "qqqqqqqq", "check": "用户名不符合规则"},
        {"user": "aaa"*10, "password": "qqqqqqqq", "check": "用户名不符合规则"},
        {"user": "aaaaaa", "password": "", "check": "缺少用户名或密码"},
        {"user": "aaaaaa", "password": "aaaaaaaa", "check": "用户名或密码错误"}
    ]

