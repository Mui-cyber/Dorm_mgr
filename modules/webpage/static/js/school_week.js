function get_school_week()
{
    let date_data=get_date();
    const data_from_localStorage=localStorage.getItem("school_week");   // 从localStorage中获取数据，这种东西不需要每次刷新界面就去源站获取
    let current_week = undefined;   //当前教学周
    if (data_from_localStorage == null)
    {
        update_school_week();
    }
    else 
    {
        let parsed_data = JSON.parse(data_from_localStorage);
        if (parsed_data.date_data != date_data)
        {
            update_school_week();
        }
        else
        {
            current_week = parsed_data.current_week;
        }
    }
    document.querySelector("#current_week").innerHTML=current_week;
}

function update_school_week()
{
    $.ajax({
        url: '/api/get_school_week', 
        method: 'POST',
        dataType: 'html',
        success: function(response) {
            // 查找目标内容
            let decoded_data = JSON.parse(response);
            if (decoded_data.status=="failed")
            {
                show_toast("时间模块","出错: API返回数据出错(返回当前周数)","bg-danger"); 
            }
	        document.querySelector("#current_week").innerHTML=decoded_data.msg;
	        write_school_week_to_localStorage(get_date(),decoded_data.msg); 
        },
        error: function(xhr, status, error) {
            show_toast("时间模块","出错: "+error,"bg-danger");
            console.error('Error fetching data:', error);
        }
    });
}

function write_school_week_to_localStorage(date_data, current_week)
{
    let parsed_data = new Object();
    parsed_data.date_data=date_data;
    parsed_data.current_week=current_week;
    let item=JSON.stringify(parsed_data);
    console.log("教学周数据更新",item);
    localStorage.setItem("school_week",item);
}

function get_date()
{
    const date=new Date();
    return date.getFullYear().toString()+(date.getMonth()+1).toString()+date.getDay();
}
