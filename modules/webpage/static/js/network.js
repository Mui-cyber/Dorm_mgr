function change_to_campus_network()
{
    let choice=confirm("你确定要把宿舍网络切换到【校园网】？");
    if (choice) {
        $.ajax({
            url: '/api/change_network_to_campus',
            method: 'POST',
            dataType: 'html',
            success: function(response) {

            },
            error: function(xhr, status, error) {
		show_toast("网络模块","出错: "+error,"bg-danger");
                console.log('Error fetching data:'+ error)
            }
        });
        show_toast("网络模块","切换请求已经发送","bg-success");
        update_isp_status();
    }
    else
    {
        show_toast("网络模块","切换请求取消","bg-secondary");
    }
}

function change_to_isp_network()
{
    let choice=confirm("你确定要把宿舍网络切换到绑定的运营商？");
    if (choice) {
        $.ajax({
            url: '/api/change_network_to_isp',
            method: 'POST',
            dataType: 'html',
            success: function(response) {

            },
            error: function(xhr, status, error) {
                show_toast("网络模块","出错: "+error,"bg-danger");
                console.log('Error fetching data:'+ error);
            }
        });
        show_toast("网络模块","切换请求已经发送","bg-success");
        update_isp_status();
    }
    else
    {
        show_toast("网络模块","切换请求取消","bg-secondary");
    }
}

let not_notified=true;

function update_isp_status()
{
    $.ajax({
        url: '/api/get_isp',
        method: 'POST',
        dataType: 'html',
        success: function(response) {
            let decoded_data = JSON.parse(response);
            if (decoded_data.status=="failed")
            {
                show_toast("网络模块","出错: API返回数据出错(请求路由器IP)","bg-danger"); 
                return;
            }
            document.querySelector("#isp").innerHTML=decoded_data.msg;
            if (response=="null")
            {
                document.querySelector("#isp").innerHTML="检查失败(未登录)";
                if (not_notified)
                {
                    show_toast("网络模块","网络未登录，请登录！","bg-danger");
                    not_notified=false;
                }
            }
            else
            {
                not_notified=true;
            }
        },
        error: function(xhr, status, error) {
            show_toast("网络模块","出错: "+error,"bg-danger");
            console.log('Error fetching data:'+ error);
        }
    });
}

function update_router_ip()
{
    $.ajax({
        url: '/api/get_router_ip',
        method: 'POST',
        dataType: 'html',
        success: function(response) {
            let decoded_data = JSON.parse(response);
            if (decoded_data.status=="failed")
            {
                show_toast("网络模块","出错: API返回数据出错(请求路由器IP)","bg-danger"); 
            }
            document.querySelector("#router-ip").innerHTML=decoded_data.msg;
        },
        error: function(xhr, status, error) {
            show_toast("网络模块","出错: "+error,"bg-danger");
            console.log('Error fetching data:'+ error);
        }
    });
}

function update_user_ip()
{
    $.ajax({
        url: '/api/get_user_ip',
        method: 'POST',
        dataType: 'html',
        success: function(response) {
            let decoded_data = JSON.parse(response);
            if (decoded_data.status=="failed")
            {
                show_toast("网络模块","出错: API返回数据出错(请求用户IP)","bg-danger"); 
            }
            document.querySelector("#user-ip").innerHTML=decoded_data.msg;
        },
        error: function(xhr, status, error) {
            show_toast("网络模块","出错: "+error,"bg-danger");
            console.log('Error fetching data:'+ error);
        }
    });
}

function update_network_module()
{
    update_user_ip();
    update_router_ip();
    update_isp_status();
}