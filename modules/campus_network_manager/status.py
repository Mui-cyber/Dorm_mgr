import requests
import json

from modules.static_variables import USER_AGENT

headers = {
    'User-Agent': USER_AGENT
}

# 获取ISP
def get_isp():
    # 定义返回JSON的数据
    status="failed"
    msg="null"
    
    # 抓取数据
    response = requests.get("http://10.100.1.5/eportal/InterFace.do?method=getOnlineUserInfo", headers=headers)

    # 分析数据
    if response.status_code == 200:
        meta_data = json.loads(response.content)
        status="success"
        msg=meta_data["service"]
    else:
        msg=f"请求失败，状态码: {response.status_code}"

    return json.dumps({"status":status,"msg":msg})

# 获取路由器IP
def get_router_ip():
    # 定义返回JSON的数据
    status="failed"
    msg="null"
    
    # 抓取数据
    response = requests.get("http://10.100.1.5/eportal/InterFace.do?method=getOnlineUserInfo", headers=headers)

    # 分析数据
    if response.status_code == 200:
        meta_data = json.loads(response.content)
        status="success"
        msg=meta_data["userIp"]
    else:
        msg=f"请求失败，状态码: {response.status_code}"

    return json.dumps({"status":status,"msg":msg})