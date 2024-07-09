function write_to_clipboard(element)
{
    // 获取按钮内的数据
    var dataToCopy = element.innerHTML;
    show_toast("网络模块",dataToCopy);

/*
    // 使用 Clipboard API 将数据复制到剪切板
    navigator.clipboard.writeText(dataToCopy).then(function() {
        console.log('数据已成功复制到剪切板');
        alert('数据已成功复制到剪切板');
    }).catch(function(err) {
        console.error('复制到剪切板失败', err);
        alert('复制到剪切板失败');
    });
*/
}
