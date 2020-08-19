#! /usr/bin/python
# -*- coding: utf-8 -*-

import time
from decimal import Decimal
import datetime

class CountingTimer(object):
    
    def __init__(self):
        self.begin_time_real = None
        self.end_time_real = None
        
        self.begin_time_cpu = None
        self.end_time_cpu = None

    def begin(self):
        self.begin_time_real = time.time()
        self.begin_time_cpu = time.clock()
        
    def end(self):
        self.end_time_real = time.time()
        self.end_time_cpu = time.clock()
    
    def diff(self):
        self.diff_real = float(Decimal(self.end_time_real - self.begin_time_real).quantize(Decimal('0.00')))
        self.diff_cpu = float(Decimal(self.end_time_cpu - self.begin_time_cpu).quantize(Decimal('0.00')))
        return self.diff_real, self.diff_cpu
    
    def current(self):
        now_stamp = time.time()
        timeArray = time.localtime(now_stamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

def get_timedelta_from_string(timedelta_string):
    if "day" in timedelta_string and "," in timedelta_string:
        day_index = timedelta_string.find("day")
        day = int(timedelta_string[:day_index])
        hour_begin_index = timedelta_string.find(",")
        hour_index = timedelta_string.find(":")
        hour = int(timedelta_string[hour_begin_index+1: hour_index])
    else:
        day = 0
        hour_index = timedelta_string.find(":")
        hour = int(timedelta_string[0: hour_index])

    minute_index = timedelta_string.find(":", hour_index + 1)
    second_index = timedelta_string.find(".")

    minute = int(timedelta_string[hour_index + 1: minute_index])
    if second_index > 0:
        second = int(timedelta_string[minute_index + 1: second_index])
        microsecond_str = timedelta_string[second_index + 1:].strip()
        microsecond = int(microsecond_str) * 10^(6-len(microsecond_str))
    else:
        second = int(timedelta_string[minute_index + 1:])
        microsecond = 0
        
    #zhangyu：其实这里的microsecond，是帧，而不是毫秒
    delta = datetime.timedelta(days=day, hours=hour, minutes=minute, seconds=second, microseconds=microsecond)
#     delta = datetime.timedelta(days=day, hours=hour, minutes=minute, seconds=second)
    return delta

def get_seconds_from_string(timedelta_string):
    if "day" in timedelta_string and "," in timedelta_string:
        day_index = timedelta_string.find("day")
        day = int(timedelta_string[:day_index])
        hour_begin_index = timedelta_string.find(",")
        hour_index = timedelta_string.find(":")
        hour = int(timedelta_string[hour_begin_index+1: hour_index])
    else:
        day = 0
        hour_index = timedelta_string.find(":")
        hour = int(timedelta_string[0: hour_index])

    minute_index = timedelta_string.find(":", hour_index + 1)
    minute = int(timedelta_string[hour_index + 1: minute_index])
    second = float(timedelta_string[minute_index+1:])
    total_seconds = (day * 24 + hour) * 3600 + minute * 60 + second
    return total_seconds

def get_datetime_from_string(datestr, delta=None):
    if "." in datestr:
        datetime_format = '%Y-%m-%d %H:%M:%S.%f'
    else:
        datetime_format = '%Y-%m-%d %H:%M:%S'
    date_time = datetime.datetime.strptime(datestr, datetime_format)
    if delta is not None:
        time_delta = get_timedelta_from_string(delta)
        date_time = date_time + time_delta
    return date_time