
import requests
url = 'http://127.0.0.1:8000/test_jmeter'
data = {
    'a':'123',
    'b':'23',
}
r = requests.post(url,data)
print(r.json())
r_data = r.json()
print(r_data['sum'])

