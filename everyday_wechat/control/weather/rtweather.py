# coding=utf-8
"""
https://github.com/MZCretin/RollToolsApi#获取特定城市今日天气
获取特定城市今日天气
"""
import requests

__all__ = ['get_rttodayweather']


# {"code":1,"msg":"数据返回成功","data":{"address":"广西壮族自治区 桂林市 全州县",
# "cityCode":"450324","temp":"26℃","weather":"晴","windDirection":"东北","windPower":"≤3级",
# "humidity":"58%","reportTime":"2019-06-14 10:49:37"}}

def get_rttodayweather(cityname, app_token):
    """
    获取特定城市今日天气
     https://github.com/MZCretin/RollToolsApi#获取特定城市今日天气
    :param cityname:str 传入你需要查询的城市，请尽量传入完整值，否则系统会自行匹配，可能会有误差
    :return:str 天气(2019-06-12 星期三 晴 南风 3-4级 高温 22.0℃ 低温 18.0℃ 愿你拥有比阳光明媚的心情)
    """
    print('获取 {} 的天气...'.format(cityname))
    try:
        resp = requests.get('https://www.mxnzp.com/api/weather/forecast/{}?app_id={}&app_secret={}'.format(cityname, app_token['app_id'], app_token['app_secret']))
        if resp.status_code == 200:
            content_dict = resp.json()
            if content_dict['code'] == 1:
                data_dict = content_dict['data']
                # print(data_dict, 'data_dict')
                address = data_dict['address'].strip()
                forecast = data_dict['forecasts'][0]

                list_data = []
                for x in [address, forecast['date'], forecast['dayWeather'], forecast['dayTemp']]:
                    list_data.append(x)

                return_text = ' '.join(list_data)
                # print(return_text)
                return return_text
            else:
                print('获取天气失败:{}'.format(content_dict['msg']))
                # return None
        print('获取天气失败。')
    except Exception as exception:
        print(str(exception))
        # return None
    # return None


get_today_weather = get_rttodayweather

if __name__ == '__main__':
    cityname = '香港'
    weather = get_today_weather(cityname)
    pass
