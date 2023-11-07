var mac_flag=1;         //播放器版本
var mac_second=5;       //播放前预加载广告时间 1000表示1秒
var mac_width="100%";      //播放器宽度
var mac_height=260;     //播放器高度
var mac_widthpop=704;   //弹窗窗口宽度
var mac_heightpop=566;  //弹窗窗口高度
var mac_showtop=1;     //美化版播放器是否显示头部
var mac_showlist=0;     //美化版播放器是否显示列表
var mac_autofull=0;     //是否自动全屏,0否,1是
var mac_buffer="http://m.sodyy.com/html/buffer.html";     //缓冲广告地址
var mac_prestrain="http://pan.poorli.com/html/prestrain.html";  //预加载提示地址
var mac_colors="000000,F6F6F6,F6F6F6,333333,666666,FFFFF,FF0000,2c2c2c,ffffff,a3a3a3,2c2c2c,adadad,adadad,48486c,fcfcfc";   //背景色，文字颜色，链接颜色，分组标题背景色，分组标题颜色，当前分组标题颜色，当前集数颜色，集数列表滚动条凸出部分的颜色，滚动条上下按钮上三角箭头的颜色，滚动条的背景颜色，滚动条空白部分的颜色，滚动条立体滚动条阴影的颜色 ，滚动条亮边的颜色，滚动条强阴影的颜色，滚动条的基本颜色
var mac_show={},mac_show_server={}; //播放器名称,服务器组地址
//缓存开始
mac_show["iva"]="①号线路";mac_show["xigua"]="西瓜影音";mac_show["xfplay"]="先锋影音";mac_show["jjvod"]="吉吉影音";mac_show["fvod"]="肥佬影音";mac_show["ffhd"]="非凡影音";mac_show["niba"]="泥巴影音";mac_show["kkhd"]="可可影音";mac_show["SNSPlay"]="SNSPlay";mac_show["kankan"]="迅雷看看";mac_show["gvod"]="秒拍mm";mac_show["cool"]="酷播cool";mac_show["qvod"]="快播qvod";mac_show["baidu"]="mm";mac_show["youku"]="优酷视频";mac_show["56"]="我乐视频";mac_show["tudou"]="土豆视频";mac_show["ku6"]="酷6视频";mac_show["qq"]="腾讯视频";mac_show["sohu"]="搜狐视频";mac_show["joy"]="⑬号线路";mac_show["qiyi"]="奇艺视频";mac_show["letv"]="乐视视频";mac_show["funshion"]="风行视频";mac_show["tudouhd"]="土豆(高清)";mac_show["sohuhd"]="搜狐(高清)";mac_show["ku6hd"]="mmsid";mac_show["sinahd"]="baiduyun";mac_show["pptv"]="pptv";mac_show["swf"]="Flash文件";mac_show["flv"]="Flv文件";mac_show["twqy"]="tw云线路";mac_show["86con"]="云播①号";mac_show["h5mp4"]="h5mp4";mac_show["opentv"]="opentv";mac_show["tianyi"]="tianyi线路";mac_show["mp4"]="mp线路";mac_show["86con2"]="云播②号";mac_show["weiyun"]="云播③号";mac_show["ugsoss"]="云播⑤号";mac_show["apoapi"]="云播⑥号";mac_show["hlsyun"]="云播⑦号";mac_show["woyun"]="云播④号";mac_show["to"]="tu线路";mac_show["vqmtv"]="vqmtv";mac_show["migu"]="migu";mac_show["59ykun"]="极速线路";mac_show["acm3"]="⑥号线路";mac_show["ckle"]="⑦号线路";mac_show["acfun"]="⑧号线路";mac_show["1905"]="1905";mac_show["ykun"]="⑤号线路";mac_show["uck"]="④号线路";mac_show["ckplayer"]="②号线路";mac_show["ck"]="③号线路";mac_show["qqqy"]="⑩号线路";mac_show["bilibili"]="⑨号线路";mac_show["imya"]="⑭号线路";mac_show["tou"]="⑮号线路";mac_show["ckmgtv"]="⑪号线路";mac_show["m4"]="m4视频";mac_show["m3u8"]="u8视频";mac_show["vipyouku"]="⑫号线路";mac_show["cksohu"]="sohu视频";mac_show["real"]="RealPlaer播放器";mac_show["media"]="MediaPlayer播放器";mac_show["link"]="外链数据";mac_show_server["webplay"]="maccmsc.com";
//缓存结束