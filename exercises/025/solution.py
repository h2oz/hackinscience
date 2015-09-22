# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:33:36 2015

@author: A
"""
import datetime
i = datetime.datetime.now()
# print("Current date & time = %s" % i)
# print("Date and time in ISO format = %s" % i.isoformat() )
# print("Current year = %s" %i.year)
# print("Current month = %s" %i.month)
# print("Current date (day) =  %s" %i.day)
print("Today is %s-0%s-%s" % (i.day, i.month, i.year), end='')
print(" and it is %s:0%s:%s" % (i.hour, i.minute, i.second))
# print("Current hour = %s" %i.hour)
# print("Current minute = %s" %i.minute)
# print("Current second =  %s" %i.second)
# print("hh:mm:ss format = %s:%s:%s" % (i.hour, i.month, i.second) )
# my_dt_ob = datetime.datetime.now()
