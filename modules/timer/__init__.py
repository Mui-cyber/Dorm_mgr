import schedule
import time

from modules.campus_network_manager import campus_network_login
from modules.elec_graph import refresh_graph

__all__=["register_schedule"]

def register_schedule():
    schedule.every(15).minutes.do(campus_network_login)
    schedule.every().day.at("06:30").do(refresh_graph)

    while True:
        # 检查并运行所有到期的任务
        schedule.run_pending()
        # 暂停一段时间以避免过度占用CPU
        time.sleep(1)

print("成功加载定时器模块")
