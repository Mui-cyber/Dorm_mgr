import re
import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from modules.static_variables import USER_AGENT
def get_elec_data(STU_ID, STU_PASSWORD):

    # UA，建议改为浏览器的UA
    custom_user_agent = USER_AGENT

    # 登录页面的URL
    login_url = 'http://xyfw.xujc.com/dfcx/'

    # 验证登录的URL
    authentication_url = 'http://xyfw.xujc.com/dfcx/index.php?c=Login&a=login'

    # 登录表单数据（账号和密码）
    login_data = {
        'username': STU_ID,
        'password': STU_PASSWORD
    }

    # 创建一个会话，以便在多次请求之间共享Cookie
    session = requests.Session()

    session.headers.update({'User-Agent': custom_user_agent})

    # 发送GET请求以获取登录页面，获取PHPSESSION的Cookie
    login_page = session.get(login_url)

    # 发送POST请求进行登录
    login_response = session.post(authentication_url, data=login_data)

    # 检查登录是否成功（可以根据响应内容或状态码来判断）
    if re.search('密码验证错误', login_response.text):
        exit()

    # 获取当前日期
    current_date = datetime.now()

    # 查询天数
    calc_days = 7

    # 计算{calc_days}天前的日期
    eight_days_ago = current_date - timedelta(days=calc_days)

    # 格式化日期为字符串，例如 "2023-10-09"
    current_date_str = current_date.strftime("%Y-%m-%d")
    eight_days_ago_str = eight_days_ago.strftime("%Y-%m-%d")

    # 定义电费查询URL的地址
    elec_query_url = f'http://xyfw.xujc.com/dfcx/index.php?c=Dfcx&a=ydjl&start={eight_days_ago_str}&end={current_date_str}&submit=%B2%E9+%D1%AF'

    # 发送GET请求
    response = session.get(elec_query_url)

    # 使用Beautiful Soup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到表格
    table = soup.find('tbody')

    # 找到所有行
    rows = table.find_all('tr')

    # 创建一个空的列表来存储用量（元）数据
    usage_data = []
    date_data = []

    # 遍历每一行，跳过表头行
    for row in rows:
        cells = row.find_all('td')
        usage_element = cells[3]
        usage_value = usage_element.get_text(strip=True)
        usage_data.insert(0, usage_value)

        date_element = cells[0]
        date_value = date_element.get_text(strip=True)
        date = datetime.strptime(date_value, '%Y-%m-%d')

        # 加1天
        new_date = date + timedelta(days=1)

        # 将datetime对象转换为字符串
        new_date_string = new_date.strftime('%Y-%m-%d')
        date_data.insert(0, new_date_string)

    date_data.append("remain_value")
    usage_data.append(rows[0].find_all('td')[4].get_text(strip=True))

    remain_data=rows[0].find_all('td')[4].get_text(strip=True)

    data_dict = dict(zip(date_data,usage_data))

    data_dict['remain_value'] = remain_data

    return json.dumps(data_dict)
