from threading import Thread
import time

import modules.webpage as webpage_daemon
import modules.elec_graph as elec_graph
import modules.timer as total_timer
import modules.campus_network_manager as network_mgr

__all__ = ["run"]

def startup_refresh_graph():
    time.sleep(5)
    elec_graph.refresh_graph()

def run():
    network_mgr.custom_isp_network_login()
    # 把电力图表画出来
    elec_graph_thread = Thread(target=startup_refresh_graph)
    elec_graph_thread.start()

    # 启动调度器线程
    timer_thread = Thread(target=total_timer.register_schedule)
    timer_thread.start()

    # 启动 Flask 线程
    flask_thread = Thread(target=webpage_daemon.run_daemon)
    flask_thread.start()

    # 等待两个线程结束
    elec_graph_thread.join()
    timer_thread.join()
    flask_thread.join()

print("启动调度器")