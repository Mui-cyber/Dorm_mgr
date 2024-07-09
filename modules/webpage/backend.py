from flask import Blueprint, request
import requests
import json
import re

from modules.static_variables import USER_AGENT
from modules.campus_network_manager import get_isp, get_router_ip, isp_network_login, campus_network_login, campus_network_logout

backend_blueprint = Blueprint('backend', __name__)

headers = {
    'User-Agent': USER_AGENT
}

# 定义route，供前端请求

# 获取教学周
@backend_blueprint.route('/api/get_school_week', methods=['POST'])
def get_school_week():

    # 定义返回JSON的数据
    status="failed"
    msg="null"

    # 抓取数据
    response = requests.get("https://www.xujc.com/calendar/hr.html", headers=headers)

    # 分析数据
    if response.status_code == 200:
        # 使用正则表达式提取周数
        match = re.search(r'<font[^>]*>(.*?)</font>', str(response.content.decode('utf-8')))
        if match:
            status="success"
            msg=match.group(1)
        else:
            msg="周数提取失败"
    else:
        msg=f"请求失败，状态码: {response.status_code}"

    return json.dumps({"status":status,"msg":msg})

# 获取ISP
@backend_blueprint.route('/api/get_isp', methods=['POST'])
def bb_get_isp():
    return get_isp()

# 获取路由器IP
@backend_blueprint.route('/api/get_router_ip', methods=['POST'])
def bb_router_ip():
    return get_router_ip()

# 获取用户IP
@backend_blueprint.route('/api/get_user_ip', methods=['POST'])
def get_user_ip():
    
    # 定义返回JSON的数据
    status="failed"
    msg="null"

    status="success"
    msg=request.remote_addr

    return json.dumps({"status":status,"msg":msg})

# 切换到绑定运营商
@backend_blueprint.route('/api/change_network_to_isp', methods=['POST'])
def change_network_to_isp():
    campus_network_logout()
    isp_network_login()
    return "Done"

# 切换到校园网
@backend_blueprint.route('/api/change_network_to_campus', methods=['POST'])
def change_network_to_campus():
    campus_network_logout()
    campus_network_login()
    return "Done"

# 获取天气(天气的API需要自己写，这里省略)
@backend_blueprint.route('/api/get_weather', methods=['POST'])
def get_weather():
    pass

