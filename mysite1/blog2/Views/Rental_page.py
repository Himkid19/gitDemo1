from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from blog2.models import HouseInfo,monthly_pay,UserProfile,Application_list
from django.contrib.auth.models import User,Group
from mysite1 import settings
from alipay import AliPay
import os


def display_house_list(request):
    house_list = HouseInfo.objects.all()
    return render(request,'rental page/house_msg_list.html',locals())

def house_detail(request,id):
    detail = HouseInfo.objects.get(id=id)
    return render(request,"rental page/house_detail.html",locals())


def Check_account(request):
    pass

def my_paying_for(request):
    try:
        house_obj = HouseInfo.objects.get(user__username=request.user.username)
        print(house_obj.house_no)
        try:
            payment_check = monthly_pay.objects.filter(house_no=house_obj)
        except Exception as e:
            payment_check = None
            print(e)
    except Exception as e:
        msg = '未安排房屋信息，请联系房主'
    return render(request,'rental page/rental_payment_page.html',locals())

def payment_detail(reuqest,pay_id):
    pay_obj = monthly_pay.objects.get(id=pay_id)
    return render(reuqest,'rental page/payment_detail.html',locals())

def alipay_page(request,order_id,total):
    house_no = str(monthly_pay.objects.get(id=order_id).house_no)

    alipay = AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url=None,
        app_private_key_path=os.path.join(settings.BASE_DIR,'keys/pri.txt'),
        alipay_public_key_path=os.path.join(settings.BASE_DIR,'keys/pub.txt'),
        sign_type="RSA2",
        debug=False  #True时在生产环境中
    )


    order_string = alipay.api_alipay_trade_page_pay(
                out_trade_no=order_id,  #订单id
                total_amount=total, #支付宝总金额
                subject="Rental management : %s" % (house_no), #订单标题
                return_url='http://127.0.0.1:8000/index/may_payment/pay_detail='+order_id,
                notify_url=None
    )
    pay_url = settings.ALIPAY_URL+order_string
    try:
        response = alipay.api_alipay_trade_query(order_id)
    except Exception as e:
        print(e)
    # 注册生产后 进行操作
    return redirect(pay_url)

def my_apply(request):
    apply_obj = Application_list.objects.all()
    return render(request,'rental page/my_application_page.html',locals())
def post_application_info(request):
    username = request.user.username
    user_obj = User.objects.get(username=username)
    type = request.POST.get('type')
    content = request.POST.get('content')
    remark = request.POST.get('remark')
    try:
        apply_obj = Application_list.objects.get(username=username)

    except:
        apply_obj = ''
    try:
        Application_list.objects.create(username=user_obj,type=type,content=content,remark=remark,status='0')
        return JsonResponse({'code':'0','error_msg':''})

    except Exception as e:
        print(e)

        return JsonResponse({'code':'1','error_msg':str(e)})
