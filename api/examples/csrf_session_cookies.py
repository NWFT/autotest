import requests

"""
Session Authentication: 
1. Get CSRF token
2. Request with token and get token in cookie
3. New request with token cookies
"""

"""
e-commerce site:
1. User login page, get CSRF token
2. Save token in Session instance, and send request with token/username/password
3. Get 'sessionid' and 'username' in cookie
4. Send new requests with 'sessionid'
"""
login_url = "http://www.alex-info.ca:8000/login/"
username = "aaaaaa"
password = "qqqqqqqq"

# create a session instance
client = requests.Session()

# 1 access login page, get CSRF token
client.get(login_url)
if 'csrftoken' in client.cookies:
    csrf_token = client.cookies['csrftoken']
else:
    csrf_token = ""

# 2 login request with token
if csrf_token:
    login_data = dict(username=username, password=password, csrfmiddlewaretoken=csrf_token)
else:
    login_data = dict(username=username, password=password)
res = client.post(login_url, data=login_data)

# sessionid after login
print(client.cookies['sessionid'])
# username in cookie
print(client.cookies['username'])

# 3 new request with sessionid
browser_history_url = "http://www.alex-info.ca:8000/browse_histories/"
response = client.get(browser_history_url)
print(response.json())

