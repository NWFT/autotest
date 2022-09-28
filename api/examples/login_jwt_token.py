import requests

"""
1. Login with username and password
2. Save jwt_token
3. New requests with jwt_token
"""

"""
1. Login api
API:
Request:    POST /paymall_admin/authorizations
            Header: application/json
            Body Schema:
                username *
                password *
Response: 
            Status_code: 200
            Msg body:
            {
            "refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NDQ4NDY4OCwiaWF0IjoxNjY0Mzk4Mjg4LCJqdGkiOiJjODJmMzM1OTcwYTU0YWM1OGMxYzMyYzg5MTExMWRmZiIsInVzZXJfaWQiOjEzLCJ1c2VybmFtZSI6ImFhYWFhYSJ9.Xyt_1lA6Q8ckTl4oaeYprcHskotducMm38SZu85ABiE",
            "access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY0Mzk4NTg4LCJpYXQiOjE2NjQzOTgyODgsImp0aSI6IjY2MWI0ZmVjMDFiYzQ2OTI4ZjE5OTBmNGMyZTBiMTk2IiwidXNlcl9pZCI6MTMsInVzZXJuYW1lIjoiYWFhYWFhIn0._wvuwYXbkBo1Ky_NVWt46LQ8fRbNJdXQ65dMiOze6UY"}
            }
            Status_code: 401
            Msg body:
            {"detail":"No active account found with the given credentials"}
"""
# Login request path
url = "http://www.alex-info.ca:8000/paymall_admin/authorizations/"

payload = {"username": "aaaaaa", "password": "qqqqqqqq"}
headers = {
    'Content-Type': 'application/json'
}
# response after login
response = requests.request("POST", url, headers=headers, json=payload)

# 2. save token
resp_dict = response.json()
access_token = resp_dict['access']

# 3. new requests
"""
GET /paymall_admin/statistical/total_count/
Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGci...
"""
headers["Authorization"] = f"JWT {access_token}"
count_url = "http://www.alex-info.ca:8000/paymall_admin/statistical/total_count/"

count_resp = requests.request("GET", count_url, headers=headers)
print(count_resp.json())
