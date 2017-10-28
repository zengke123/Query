# Query

命令行查看工具
======
支持火车票查询、电影查询、天气查询<br>
------
Options:
    
    火车票查询
    -T <from> <to> <date> 
        -g      高铁
        -d      动车
        -t      特快
        -k      快速
        -z      直达
    电影查询
    -M          
        -n      正在上映
        -c      即将上映
        -p      实时票房
    天气查询,支持地名解析
    -W <location>
    帮助
    -h,--help   


Example:

    query -T  北京 上海 2017-10-24
    query -Tdg  成都 南京 2017-10-24
    query -M
    query -Mp 查看实时票房
    query -Mc 即将上映电影
    query -W  四川大学
"""
 ![image](https://github.com/zengke123/Query/raw/master/image/info.png)
 
 安装
 ------
 python3 setup install
 










