function time(){
    var vWeek,vWeek_s,vDay;
    vWeek = ["星期天","星期一","星期二","星期三","星期四","星期五","星期六"];
    var date =  new Date();
    year = date.getFullYear();
    month = date.getMonth() + 1;
    day = date.getDate();
    hours = date.getHours();
    minutes = date.getMinutes();
    seconds = date.getSeconds();
    vWeek_s = date.getDay();
    if (minutes < 10)
            minutes = "0" + minutes
    if (seconds < 10)
            seconds = "0" + seconds
    document.getElementById("current_date").innerHTML =year + "年" + month + "月" + day + "日" +"&nbsp;&nbsp;&nbsp;"+ vWeek[vWeek_s];
    document.getElementById("current_time").innerHTML =  + "\t" + hours + ":" + minutes +":" + seconds + "\t";
};
