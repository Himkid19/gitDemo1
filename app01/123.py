# import requests,json
#
# api_url = "https://openapi.58.com/v2/info/fang/post"
# data = json.dumps({
#     "access_token": "4c5d8f6ee8678ed530ecbcc91c56f636",
#     "openid": "19fcfdaa6aad88c7f1b79f3219c8000a",
#     "cate_id": "8",
#     "local_id": "2721",
#     "title": "平西小区2室，小户型，屋内阳光充足，周边设施齐全便利test6",
#     "content": "test6房屋向南，阳光充足，临近地铁，交通便利。附近有菜市场，超市，大型商场，生活便利、舒适。真实房源，快来打电话吧。",
#     "phone": "13436890361",
#     "effectiveDate": "2017-05-30",
#     "email": "com",
#     })
# r = requests.post(url=api_url,data=data)
# print(r.json())

import django
print(django.get_version())