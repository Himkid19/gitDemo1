from django.test import TestCase
import requests,json
from alipay import AliPay
import os
import settings
# Create your tests here.

# 房天下 注册申请接口调用
# url = "https://openapi.fang.com/unity/authenticate"
# data = {
#     'userName':'15818183032',
#     'pwd':'a419832308',
#     'keyid':'18661740',
# }
#
# j = requests.post(url,data)
# print(j.json())

alipay = AliPay(
    appid="2016092900622067",
    app_notify_url=None,
    app_private_key_path=os.path.join(settings.BASE_DIR,'keys/pri.txt'),
    alipay_public_key_path=os.path.join(settings.BASE_DIR,'keys/pub.txt'),
    sign_type="RSA2",

)


order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no='11',  #订单id
            total_amount='100', #支付宝总金额
            subject="天天生鲜%s"%"11", #订单标题
            return_url=None,
            notify_url=None
)
pay_url = "https://openapi.alipaydev.com/gateway.do?"+order_string
print(pay_url)



if __name__ == '__main__':
    alipay



