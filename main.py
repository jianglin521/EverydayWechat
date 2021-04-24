# coding=utf-8
import pyperclip
import time
# import json
import os
import requests
from everyday_wechat.utils.data_collection import (
    get_weather_info,
    get_dictum_info,
    get_diff_time,
    get_calendar_info,
    get_constellation_info
)
from everyday_wechat.control.airquality.air_quality_aqicn import (
    get_air_quality
)
from everyday_wechat.utils import config

__all__ = ['run', 'delete_cache']

def send_alarm_msg():
    print('\n获取消息...')
    gf = config.get('alarm_info').get('girlfriend_infos')[0]
    is_tomorrow = gf.get('is_tomorrow', False)
    # calendar_info = get_calendar_info(gf.get('calendar'), gf.get('app_token'), is_tomorrow)
    weather = get_weather_info(gf.get('city_name'), gf.get('app_token'), is_tomorrow)
    horoscope = get_constellation_info(gf.get("horescope"), is_tomorrow)
    dictum = get_dictum_info(gf.get('dictum_channel'))
    diff_time = get_diff_time(gf.get('start_date'), gf.get('start_date_msg'))
    air_quality = get_air_quality(gf.get('air_quality_city'))
    sweet_words = gf.get('sweet_words')

    list_data = []
    for x in [weather, air_quality, horoscope, dictum, diff_time, sweet_words]:
        if x:
            list_data.append(x)
            
    send_msg = '  \n'.join(list_data) # 必须添加两个空格加换行
    print('\n' + send_msg + '\n')
    pyperclip.copy(send_msg)
    with open('./result.txt', 'w', encoding='utf-8') as f:
        f.write(send_msg)
    form = {
        'title': '每日一句',
        'desp': send_msg
    }
    send_key = os.environ.get('SEND_KEY')
    resp = requests.post('https://sctapi.ftqq.com/{}.send'.format(send_key), form)
    if resp.status_code == 200:
        print('发送成功！')

#    https://sctapi.ftqq.com/SCT8123T5z4jvG3LpM6ovMWPuhcqzJua.send?title=添加测试&desp=测试1111

if __name__ == '__main__':
    send_alarm_msg()
