from django.test import TestCase
import time,requests,pyDes
# Create your tests here.
import sys
import json

url = "https://api.yonyoucloud.com/apis/dst/mobilemessage/sendmessage"

headers = {
    'authoration':'apicode',
    'apicode':'ab0e67a5eb134e6d87863bbf97afb164',
    'Content-Type':'application/json',
}
data = {
    'msg':'this is test msg',
    'phone':'15818183032',
}

json.dumps(data)

j = requests.post(url=url,data=data,headers=headers)
print(j.json())