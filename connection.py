# coding=utf-8
import pandas as pd
import sqlalchemy
import settings

def GetEngineUS():
    USER = settings.ZEUS_USER
    PW = settings.ZEUS_PW
    URL = '10.131.11.81:35432/ZEUS_US-RM'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    return sqlalchemy.create_engine(url)

def run_queryUS(qry):
    return pd.read_sql(sql=qry, con=GetEngineUS())


def GetEngineFS():
    USER = settings.ZEUS_USER
    PW = settings.ZEUS_PW
    URL = '172.21.130.152:35432/ZEUS_BR-FS'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    return sqlalchemy.create_engine(url)

def run_queryFS(qry):
    return pd.read_sql(sql=qry, con=GetEngineFS())

def GetEngineCM():
    USER = settings.ZEUS_BR_CM_USER
    PW = settings.ZEUS_BR_CM_PASSWORD
    URL = '172.21.9.153:35432/ZEUS_BR-CM'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    return sqlalchemy.create_engine(url)

def run_queryCM(qry):
    return pd.read_sql(sql=qry, con=GetEngineCM())

def GetEngineAR():
    USER = settings.ZEUS_AR_USER
    PW = settings.ZEUS_AR_PASSWORD
    URL = '151.10.190.48:35432/ZEUS_AR'
    url = 'postgresql://{}:{}@{}'.format(USER,PW,URL)
    return sqlalchemy.create_engine(url)

def run_queryAR(qry):
    return pd.read_sql(sql=qry, con=GetEngineAR())