from .login import default_campus_network_login, isp_network_login
from .logout import network_logout
from .status import get_isp, get_router_ip

__all__=["campus_network_login","custom_isp_network_login","campus_network_logout","get_isp","get_router_ip"]

def custom_isp_network_login():
    isp_network_login()

def campus_network_login():
    default_campus_network_login()

def campus_network_logout():
    network_logout()

print("成功加载网络模块")