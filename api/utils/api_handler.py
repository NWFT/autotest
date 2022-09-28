import requests


def header_handler(token=None):
    """
    Generate headers for requests.
    If special header needed, put it here.
    :param token: access token after login
    :return: New header
    """
    headers = {'Content-Type': 'application/json'}
    if token:
        headers["Authorization"] = f"JWT {token}"

    return headers


def send_requests(method, url, data=None, token=None):
    """
    Get request header
    Send requests according to methods
    :param method: GET/POST/DELETE/UPDATE
    :param url: request url
    :param data: data if needed
    :param token: token after login
    :return:
    """
    headers = header_handler(token)
    if method.upper() == "GET":
        resp = requests.get(url, data, headers=headers)
    else:
        resp = requests.post(url, json=data, headers=headers)

    return resp


if __name__ == '__main__':
    url = "http://www.alex-info.ca:8000/paymall_admin/authorizations/"
    payload = {"username": "aaaaaa", "password": "qqqqqqqq"}
    resp = send_requests("POST", url, payload)

    access_token = resp.json()['access']
    count_url = "http://www.alex-info.ca:8000/paymall_admin/statistical/total_count/"
    count_resp = send_requests("GET", count_url, token=access_token)
    print(count_resp.json())