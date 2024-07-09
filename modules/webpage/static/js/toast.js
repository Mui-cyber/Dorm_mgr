function show_toast(head_msg,body_msg,head_color)
{
    if (head_color == null || head_color == undefined || head_color == "")
    {
        head_color="bg-success";
    }
    const toastLiveExample = document.getElementById('liveToast');
    const toast = new bootstrap.Toast(toastLiveExample);
    document.querySelector("#toast-main").classList="toast-header text-light";
    document.querySelector("#toast-main").classList.add(head_color);
    document.querySelector("#toast-head-msg").innerHTML=head_msg;
    document.querySelector("#toast-body-msg").innerHTML=body_msg;
    toast.show();
}
