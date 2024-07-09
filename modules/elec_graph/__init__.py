from user_conf import STU_ID, STU_PASSWORD
import os

from .get_elec_status import get_elec_data
from .gen_elec_graph import make_graph

# 获取当前目录，需要把生成的页面放到webpage的templates中
current_directory = os.path.dirname(os.path.abspath(__file__))

# 生成页面的路径
templates_save_path = os.path.join(current_directory, '..', 'webpage', 'static', 'elec_chart.html')

__all__ = ["get_graph","delete_graph","refresh_graph"]

def get_graph():
    try:
        print(current_directory)
        elec_json = get_elec_data(STU_ID, STU_PASSWORD)
        make_graph(elec_json, templates_save_path)
    except:
        print("*")
        print(r'*** 警告：用电量获取失败，请确认自己是否已经绑定宿舍或者密码是否正确，绑定地址："http://xyfw.xujc.com/dfcx/" ***')
        print("*")

def delete_graph():
    os.remove(templates_save_path)

def refresh_graph():
    try:
        delete_graph()
    except:
        None
    get_graph()

print("成功加载宿舍用电量渲染模块")
