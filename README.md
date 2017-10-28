# Query

命令行查看工具
======
支持火车票查询、电影查询、天气查询<br>
------
Options:<br>
    -h,--help   显示帮助菜单<br>
    -T          火车票查询<br>
        -g      高铁<br>
        -d      动车<br>
        -t      特快<br>
        -k      快速<br>
        -z      直达<br>

    -M          电影查询<br>
        -n      正在上映<br>
        -c      即将上映<br>
        -p      实时票房<br>

    -W          天气查询,支持地名解析<br>


Example:<br>
    query -T  北京 上海 2017-10-24<br>
    query -T  成都 南京 2017-10-24 -dg<br>
    query -M<br>
    query -Mp 查看实时票房<br>
    query -W  四川大学<br>
"""
 ![image](https://github.com/zengke123/Query/raw/master/image/info.png)
 
 安装
 ------
 python3 setup install
 










