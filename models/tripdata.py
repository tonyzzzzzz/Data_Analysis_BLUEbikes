#!/usr/bin/python
# coding:utf-8
# Tripdata Model

from sqlalchemy import Column, TEXT, INTEGER, REAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class tripdata(Base):
    __tablename__ = 'tripdata'

    id = Column(INTEGER, primary_key=True)
    tripduration = Column(INTEGER)
    starttime = Column(INTEGER)
    stoptime = Column(INTEGER)
    start_station_id = Column(INTEGER)
    end_station_id = Column(INTEGER)
    bikeid = Column(INTEGER)
    usertype = Column(TEXT)
    birth_year = Column(INTEGER)
    gender = Column(INTEGER)


