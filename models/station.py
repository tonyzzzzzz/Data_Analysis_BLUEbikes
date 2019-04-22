#!/usr/bin/python
# coding:utf-8
# Station Model

from sqlalchemy import Column, TEXT, INTEGER, REAL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class station(Base):
    __tablename__ = 'station'

    id = Column(INTEGER, primary_key=True)
    station_name = Column(TEXT)
    latitude = Column(REAL)
    longitude = Column(REAL)


