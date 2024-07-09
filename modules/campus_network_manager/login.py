import requests

from user_conf import STU_ID, CAMPUS_NET_PASSWORD, ISP
from .tools import get_url_encoded_data, load_login_var

# 登录校园网
def default_campus_network_login():
    post_login_data("校园网")

# 登录指定ISP
def isp_network_login():
    post_login_data(ISP)

# POST数据执行
def post_login_data(ISP):
    try:
        LOGIN_VAR = load_login_var()
        total_login_data = {
            'userId': get_url_encoded_data(STU_ID),
            'password': get_url_encoded_data(CAMPUS_NET_PASSWORD),
            'service': get_url_encoded_data(ISP),
            'queryString': LOGIN_VAR,
            'operatorPwd': '',
            'operatorUserId': '',
            'validcode': '',
            'passwordEncrypt': 'false'
        }
        requests.post("http://10.100.1.5/eportal/InterFace.do?method=login",data=total_login_data)
    except TypeError:
        print("*")
        print("*** 警告：登录数据发送失败 ***")
        print("*")