
# coding: utf-8
import pandas as pd
from connection import * # here use your configuration file of connection with the datebase 
import datetime as dt

run_query = run_queryFS

# -- Return current shift
def sch_turno():
    hrs = int(str(get_data())[11:13])
    if (hrs >= 7) and (hrs < 15):
        return '1'
    elif (hrs >= 15) and (hrs < 23):
        return '2'
    else:
        return '3'
    
# -- Return current date
def get_data(formato='%Y-%m-%d %H:%M:%S'):
    qry = "SELECT NOW() AS DTA_NOW"
    dta = run_query(qry)
    return dta.iloc[0]['DTA_NOW'].strftime(formato)

def get_data_sSQL():
    return time.strftime('%Y-%m-%d %H:%M:%S')

# 
def ps_date():
    psd = pd.to_datetime(get_data()) - dt.timedelta(minutes=420)
    return psd.strftime('%Y-%m-%d 00:00:00')

# -- Return last date (default=1)
def last_date(days=1):
    hj = dt.date.today()
    last = dt.date.fromordinal(hj.toordinal()-days)
    lastDay = last.strftime('%Y-%m-%d 00:00:00')
    return lastDay

def tomorrow(days=1):
    hj = dt.date.today()
    last = dt.date.fromordinal(hj.toordinal()+days)
    lastDay = last.strftime('%Y-%m-%d')
    return lastDay

def last_only_date(days=1):
    hj = dt.date.today()
    last = dt.date.fromordinal(hj.toordinal()-days)
    lastDay = last.strftime('%Y-%m-%d')
    return lastDay

#  -- Return shift begin
def inicio_turno():
    hrs = int(str(get_data())[11:13])
    if (hrs >= 7) and (hrs < 15):
        return pd.to_datetime(ps_date()).strftime('%Y-%m-%d 07:00:00')
    elif (hrs >= 15) and (hrs < 23):
        return pd.to_datetime(ps_date()).strftime('%Y-%m-%d 15:00:00')
    else:
        return pd.to_datetime(ps_date()).strftime('%Y-%m-%d 23:00:00')

def inicio_turno_ontem():
    hrs = int(str(last_date())[11:13])
    if (hrs >= 7) and (hrs < 15):
        return pd.to_datetime(last_date()).strftime('%Y-%m-%d 07:00:00')
    elif (hrs >= 15) and (hrs < 23):
        return pd.to_datetime(last_date()).strftime('%Y-%m-%d 15:00:00')
    else:
        return pd.to_datetime(last_date()).strftime('%Y-%m-%d 23:00:00')

# -- Return shift end       
def fim_turno():
    hrs = int(str(get_data())[11:13])
    if (hrs >= 7) and (hrs < 15):
        return pd.to_datetime(ps_date()).strftime('%Y-%m-%d 14:59:59')
    elif (hrs >= 15) and (hrs < 23):
        return pd.to_datetime(ps_date()).strftime('%Y-%m-%d 22:59:59')
    else:
        next_time = pd.to_datetime(get_data()) + dt.timedelta(minutes=480)
        return next_time.strftime('%Y-%m-%d 06:59:59')

def fim_turno_ontem():
    hrs = int(str(last_date())[11:13])
    if (hrs >= 7) and (hrs < 15):
        return pd.to_datetime(last_date()).strftime('%Y-%m-%d 15:00:00')
    elif (hrs >= 15) and (hrs < 23):
        return pd.to_datetime(last_date()).strftime('%Y-%m-%d 23:00:00')
    else:
        next_time = pd.to_datetime(last_date()) + dt.timedelta(minutes=480)
        return next_time.strftime('%Y-%m-%d 07:00:00')
		
# -- Return current date with no hours
def get_only_data():
    qry = "SELECT NOW() AS DTA_NOW"
    dta = run_query(qry)
    return dta.iloc[0]['DTA_NOW'].strftime('%Y-%m-%d 00:00:00')

def get_only_data_day():
    qry = "SELECT NOW() AS DTA_NOW"
    dta = run_query(qry)
    return dta.iloc[0]['DTA_NOW'].strftime('%Y-%m-%d')
	
# -- Return hours
def get_only_h():
    qry = "SELECT NOW() AS DTA_NOW"
    dta = run_query(qry)
    return int(dta.iloc[0]['DTA_NOW'].strftime('%H'))


# -- Return minutes
def get_only_m():
    qry = "SELECT NOW() AS DTA_NOW"
    dta = run_query(qry)
    return int(dta.iloc[0]['DTA_NOW'].strftime('%M'))


# -- Return seconds	
def get_only_s():
    qry = "SELECT NOW() AS DTA_NOW"
    dta = run_query(qry)
    return int(dta.iloc[0]['DTA_NOW'].strftime('%S'))

def time_past():
    if sch_turno() == '1':
        delta=420
    elif sch_turno() == '2':
        delta=900
    elif get_only_h() > 22:
        delta=1380
    else:
        delta=-60
    h = get_only_h()
    m = get_only_m()
    s = get_only_s()
    
    x = (int(h)*60 + int(m) + (int(s)/60))- delta

    return x 

	
#
def ps_date_000():
    psd = pd.to_datetime(get_data()) - dt.timedelta(minutes=420)
    return psd.strftime('%Y-%m-%d 00:00:00.000')