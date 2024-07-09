from urllib.parse import quote_plus, urlparse
from bs4 import BeautifulSoup
import requests
import re
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
login_var_path = os.path.join(current_directory, 'login_var.txt')

# 获取URL Encode后的数据
def get_url_encoded_data(data):
    return quote_plus(data)

def load_login_var():
    LOGIN_VAR = None
    if not os.path.exists(login_var_path):
        # 如果文件不存在，执行特定函数
        LOGIN_VAR = get_login_var()
        if LOGIN_VAR == "" or LOGIN_VAR == None:
            print("网络模块数据错误，需要退出网络登录再试")
        else:
            # 创建一个新文件
            with open(login_var_path, 'w') as f:
                f.write(LOGIN_VAR)
    else:   # 文件是空的
        with open(login_var_path, 'r') as f:
            LOGIN_VAR = f.readline()
            if LOGIN_VAR == "" or LOGIN_VAR == None:
               os.remove(login_var_path)
               LOGIN_VAR = get_login_var()
               if LOGIN_VAR == "" or LOGIN_VAR == None:
                    print("网络模块数据错误，需要退出网络登录再试")
    return LOGIN_VAR

def get_login_var():
    # 初始 URL
    initial_url = 'http://10.100.1.5'

    # 发送 GET 请求并自动处理重定向
    response = requests.get(initial_url)

    # 获取最终的 URL
    final_url = response.url

    # 获取最终页面内容
    final_response = requests.get(final_url)

    # 使用 BeautifulSoup 解析页面内容
    soup = BeautifulSoup(final_response.text, 'html.parser')

    # 查找第一个 <script> 标签
    script_tag = soup.find('script')

    # 如果找到了 <script> 标签
    if script_tag:
        script_content = script_tag.string

        # 使用正则表达式从 <script> 标签内容中提取 URL
        url_match = re.search(r"top.self.location.href='([^']+)'", script_content)
        if url_match:
            redirect_url = url_match.group(1)

            # 使用 urlparse 解析 URL
            parsed_url = urlparse(redirect_url)

            # 获取查询参数部分
            return parsed_url.query
    
    return None