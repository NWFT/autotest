import json

import requests

from api.utils.config_handler import conf
from api.utils.my_logger import logger


def __header_handler(token=None):
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


# process url
def __process_url(url):
    # if not start with '/', add and return full url
    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    elif url.startswith("http://") or url.startswith("https://"):
        return url
    else:
        return base_url + '/' + url


# process data
def __process_data(data):
    # if data is not None and is string
    if data is not None and isinstance(data, str):
        return json.loads(data)
    return data


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
    logger.info("Send a HTTP request.")
    headers = __header_handler(token)

    # get a full url
    url = __process_url(url)
    # transfer string into json dict, if str input
    data = __process_data(data)

    logger.info(f"HTTP Header is {headers}.")
    logger.info(f"HTTP Method is {method}.")
    logger.info(f"HTTP Url is {url}.")
    logger.info(f"HTTP request data is {data}.")

    # according 'method' to send request
    if method.upper() == "GET":
        resp = requests.get(url, data, headers=headers)
    else:  # POST currently
        resp = requests.post(url, json=data, headers=headers)

    logger.info(f"HTTP Response status code is {resp.status_code}.")
    logger.info(f"HTTP Response data is {resp.json()}.")
    return resp


if __name__ == '__main__':
    test_url = "/paymall_admin/authorizations/"
    payload = {"username": "aaaaaa", "password": "qqqqqqqq"}
    resp = send_requests("POST", test_url, payload)

    access_token = resp.json()['access']
    count_url = "/paymall_admin/statistical/total_count/"
    count_resp = send_requests("GET", count_url, token=access_token)
    print(count_resp.json())
