#! /usr/bin/env python

import sys
from jd_spider_requests import JdSeckill

if __name__ == '__main__':
    a = """
功能列表：
    1、预约商品
    2、秒杀抢购商品
    """
    print(a)

    jd_seckill = JdSeckill()
    choice_funtion = input('请选择：')
    if choice_funtion == '1':
        jd_seckill.reserve()
    elif choice_funtion == '2':
        jd_seckill.seckill_by_proc_pool()
    else:
        print('没有此功能')
        sys.exit(1)
