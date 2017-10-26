# Query
"""命令行查看工具

Usage:
    tickets [-MgdtkzTncW]  ((<from>  <to>  <date>)|()| (<city>))

Options:
    -h,--help   显示帮助菜单
    -T          火车票查询
        -g      高铁
        -d      动车
        -t      特快
        -k      快速
        -z      直达

    -M          电影查询
        -n      正在上映
        -c      即将上映

    -W          天气查询

Example:
    tickets -T 北京 上海 2017-10-24
    tickets -T 成都 南京 2017-10-24 -dg
    tickets -M
    tickets -W 四川大学
"""
