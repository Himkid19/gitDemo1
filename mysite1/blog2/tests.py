from django.test import TestCase
import time,requests,pyDes
# Create your tests here.
url = "https://openapi.fang.com/unity/authenticate"

data = {
    # 'userName':'homkid19',
    # 'pwd':'1496829295748',
    # 'keyId':18661740
}

j = requests.post(url=url,data=data)
print(j.json())