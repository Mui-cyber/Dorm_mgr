from flask import send_from_directory, render_template, Blueprint

frontend_blueprint = Blueprint('frontend', __name__)

# 把静态数据全部转移到static里面
@frontend_blueprint.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

# 根目录处理，返回index.html即可
@frontend_blueprint.route('/')
def index():
    return render_template('index.html')

# 电费页面
@frontend_blueprint.route('/elec_chart')
def elec_chart():
    return render_template('elec_chart.html')