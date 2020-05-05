import os
import time
import math
import humanize
import datetime

start_time = time.time()

def datetime_str(time_num = None, include_ms = False):
    if time_num is None:
        time_num = time.time()
    if str(type(time_num)) == "<class 'datetime.datetime'>":
        time_num = time_num.timestamp()
    timestr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_num))
    if include_ms:
        if '.' in repr(time_num):
            mlsec = (repr(time_num).split('.')[1] + '000')[:3]
        else:
            mlsec = '000'
        timestr += '.' + mlsec
    return timestr

def uptime_secs():
	tm = time.time()
	timediff = math.floor(tm - start_time)
	return timediff

def uptime_str():
	tm = time.time()
	timediff = math.floor(tm - start_time)
	uptime = humanize.naturaldelta(datetime.timedelta(seconds=timediff))
	return uptime