function get_weather()
{
    // 你可以在这里修改天气数据详情
    update_weather_data();

}

function get_btn_status(background_color,text)
{
    return '<button class="btn btn-sm '+background_color+' text-center text-light">'+text+'</button>';
}

function draw_btn_to_page(page_id,max_threshold,min_threshold,current_value,symbol)
{
    if (min_threshold == max_threshold==-1)
    {
        document.querySelector("#"+page_id).innerHTML= get_btn_status("bg-success",current_value+symbol);
        return;
    }
    if (min_threshold == max_threshold==-2)
    {
        document.querySelector("#"+page_id).innerHTML= get_btn_status("bg-warning",current_value+symbol);
        return;
    }
    if (min_threshold == max_threshold==-3)
    {
        document.querySelector("#"+page_id).innerHTML= get_btn_status("bg-danger",current_value+symbol);
        return;
    }

    if (current_value > max_threshold)
    {
        document.querySelector("#"+page_id).innerHTML= get_btn_status("bg-danger",current_value+symbol);
    }    
    else if (current_value < min_threshold)
    {
        document.querySelector("#"+page_id).innerHTML= get_btn_status("bg-warning",current_value+symbol);
    }
    else
    {
        document.querySelector("#"+page_id).innerHTML= get_btn_status("bg-success",current_value+symbol);
    }
}

function update_weather_data()
{
    return;
    let weather_data = undefined;
    $.ajax({
        url: '/api/get_weather',
        method: 'POST',
        dataType: 'html',
        success: function(response) {
            weather_data = JSON.parse(response).data;
            let forecast = weather_data.forecast[0];
            //根据需要对下列数据进行解析

            //天气预报
            let weather_forecast = forecast.type;
            draw_btn_to_page("weather_forecast",-1,-1,weather_forecast,"");

            //天气建议
            let weather_suggestion = forecast.notice;
            draw_btn_to_page("weather_suggestion",-1,-1,weather_suggestion,"");

            //当前温度
            let wendu = Number(weather_data.wendu);
            draw_btn_to_page("current_temperature",35,10,wendu,"℃");
        
            //当前湿度
            let shidu = Number(weather_data.shidu.replace("%",""));
            draw_btn_to_page("current_humidity",80,40,shidu,"%");
        
            //最高温
            let highest_temperature = forecast.high;
            draw_btn_to_page("max_temperature",-2,-2,highest_temperature,"");
            
            //最低温
            let lowest_temperature = forecast.low;
            draw_btn_to_page("min_temperature",-2,-2,lowest_temperature,"");

            //日出
            let sun_rise = forecast.sunrise;
            draw_btn_to_page("sunrise_time",-1,-1,sun_rise,"");
            
            //日落
            let sun_set = forecast.sunset;
            draw_btn_to_page("sunset_time",-1,-1,sun_set,"");

            //风向
            let wind_direction = forecast.fx;
            draw_btn_to_page("wind_direction",-1,-1,wind_direction,"");
            
            //风力
            let wind_speed = Number(forecast.fl.replace("级",""));
            draw_btn_to_page("wind_speed",8,-1,wind_speed,"级");

            //PM2.5
            let pm25 = Number(weather_data.pm25);
            draw_btn_to_page("current_pm25",9999,9999,pm25,"");
        
            //PM10
            let pm10 = Number(weather_data.pm10);
            draw_btn_to_page("current_pm10",9999,9999,pm10,"");
        
            //空气质量
            let air_quality =weather_data.quality;
            draw_btn_to_page("current_air_quality",-1,-1,air_quality,"");
            
            //空气质量
            let suggestion =weather_data.ganmao;
            draw_btn_to_page("current_air_suggestion",-1,-1,suggestion,"");
        },
        error: function(xhr, status, error) {
            show_toast("天气模块","出错: "+error,"bg-danger");
            weather_json = 'Error fetching data:'+ error;
        }
    });
    return weather_data;
}
