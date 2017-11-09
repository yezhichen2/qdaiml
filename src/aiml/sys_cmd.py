# coding=utf-8
import datetime
import json

import requests


def query_weather(city):

    url = "http://www.sojson.com/open/api/weather/json.shtml"

    try:
        resp = requests.get(url, params={"city": city})

        weather_result = json.loads(resp.text)

        weather = weather_result.get("data", {}).get("forecast", [{}])[0]

        if not weather:
            return "对不起，没有找到相关的天气情况"

        template = "{date} {city} {type} 最{high} 最{low}".format(city=city, **weather)
        return template

    except Exception as e:
        return "访问天气服务失败"

    return "访问天气服务失败"



def cur_date():
    ws = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七"}
    now = datetime.datetime.now()
    output = now.strftime("%Y年%m月%d日 星期{0} %H点%M分").format(ws.get(now.strftime("%w")))
    return output


def week_day(cn_day):
    ws = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七"}
    cn_days = {"前天":-2, "昨天": -1, "今天": 0, "明天": 1, "后天": 2}
    now = datetime.datetime.now() + datetime.timedelta(days=cn_days.get(cn_day, 0))
    output = now.strftime("%Y年%m月%d日 星期{0}").format(ws.get(now.strftime("%w")))
    return output



