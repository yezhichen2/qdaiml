# coding=utf-8

import datetime
from . import sys_cmd


class TmpExt(object):

    @classmethod
    def exts(cls, ext_ctx={}):

        def set_glb(name, val):
            ext_ctx[name] = val

        return dict(set_glb=set_glb, cur_date=sys_cmd.cur_date, week_day=sys_cmd.week_day,
                    query_weather=sys_cmd.query_weather)
