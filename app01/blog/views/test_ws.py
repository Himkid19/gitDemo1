from django.shortcuts import render,HttpResponse #引入HttpResponse
from dwebsocket.decorators import accept_websocket,require_websocket #引入dwbsocket的accept_websocket装饰器
import uuid
import json

def to_sendmsg(request):
    return render(request, 'sendmsg.html')
def to_recmsg(reuqest):
    return render(reuqest, 'recmsg.html')

@accept_websocket
def link(request):
    if request.is_websocket():
        while True:
            message = request.websocket.wait()
            if not message:
                break
            else:
                print("客户端链接成功："+str(message, encoding = "utf-8"))


def send(reuqest):
    msg = reuqest.POST.get('msg')
    print(msg)
    return HttpResponse({"msg":"success"})

def ws_temp(request):
    return render(request,'test_wc.html')


@require_websocket
def echo_once(request):
    msg = request.websocket.wait()
    request.websocket.send(msg)




def to_chat(request):

    return render(request,'to_chat.html',locals())

clients = {}

@accept_websocket
def chat(request):
    if request.is_websocket():
        userid = str(uuid.uuid1())[::8]   #替换为userid
        clients[userid] = request.websocket
#         每一个websocket链接视为一个用户
        while True:
            for i in clients:
                print(i)
            msg = request.websocket.wait()
            if not msg:
                break
            else:
                msg = str(msg,encoding="utf-8")
                if msg == "test":
                    print("websocket conntect success"+userid)
                    # 当前在线用户
                    request.websocket.send(json.dumps({"userid":userid,"type":"0","userlist":list(clients.keys())}))
                    for client in clients:
                        # 所有用户列表
                        clients[client].send(json.dumps({"user":None,"type":"0","userlist":list(clients.keys())}))
#         删除离开聊天框的用户
        if userid in clients:
            del clients[userid]
            print(userid+"离线")
            for client in clients:
                clients[client].send(json.dumps({"user":None,"type":"0","userlist":list(clients.keys())}).encode("'utf-8'"))


def msg_send(request):
    msg = request.POST.get('txt')
    userto = request.POST.get('userto')
    userfrom = request.POST.get('userfrom')
    type = request.POST.get('type')
    #  返回json中 user为空即群发；user为userid即私发;type为1表示发送信息
    if type == '1':
    #群发
        for client in clients:
            clients[client].send(json.dumps({"type":"1","data":{"msg":msg,"user":userfrom}}).encode("'utf-8'"))
    else:
    #私发(匹配useridto在clients中),对方显示
        clients[userto].send(json.dumps({"type":"1","data":{"msg":msg,"user":userfrom}}).encode("'utf-8'"))
        #私发，自己显示
        clients[userfrom].send(json.dumps({"type":"1","data":{"msg":msg,"user":userfrom}}).encode("'utf-8'"))

    return HttpResponse(json.dumps({"msg":"success"}))













