import requests


login_url = "https://45.13.119.60:2070/d7oom/login"
get_traffic = (
    "https://45.13.119.60:2070/d7oom/panel/api/inbounds/getClientTraffics/d7oom"
)

payload = {"username": "d7oom", "password": "H9Kjx5GF4nqdrb7"}

session = requests.Session()

login_response = session.post(login_url, data=payload, verify=False)


if login_response.ok:
    print(login_response.json())
else:
    print("Login failed:", login_response.status_code, login_response.text)

traffic_response = session.get(get_traffic, verify=False)

if traffic_response.json()["obj"]:
    print(traffic_response.json())
else:
    print("client data could not be find")
