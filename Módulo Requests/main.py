import requests

response = requests.get('https://www.walissonsilva.com/')
print('Status Code: ', response.status_code)
print('Header: ', response.headers)
print('Content: ', response.content)