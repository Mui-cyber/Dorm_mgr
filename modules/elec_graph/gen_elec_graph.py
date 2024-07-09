import json
import plotly.graph_objects as go
import plotly.offline as opy

def make_graph(elec_json, templates_save_path):

    # 把获取到的电力数据字典拿过来
    elec_status_dict = json.loads(str(elec_json))

    # 提取日期和电费数据
    remaining_cost = float(elec_status_dict["remain_value"])
    dates = [date for date in elec_status_dict if date != "remain_value"]
    electricity_cost = [float(value) for value in elec_status_dict.values() if value != remaining_cost]

    # 创建 Plotly 折线图
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=electricity_cost, mode='lines+markers', name='电费数据'))

    # 设置图表布局
    fig.update_layout(title='每天的电费数据', xaxis_title='日期', yaxis_title='电费',template="plotly_dark")

    # 添加剩余电费信息到图表外部标题

    if remaining_cost <=20 :
        title = f'每天的电费数据，剩余电费：{remaining_cost}元，电费不足，请及时充值'
    else:
        title = f'每天的电费数据，剩余电费：{remaining_cost}元'
    fig.update_layout(title_text=title)

    # 将图表保存为HTML文件
    html_file = templates_save_path
    opy.plot(fig, filename=html_file, auto_open=False)
