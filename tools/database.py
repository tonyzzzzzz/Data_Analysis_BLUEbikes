#!/usr/bin/python
# coding:utf-8
# sqlite3 Connector

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database(object):
    def __init__(self):
        self.__engine = create_engine('sqlite:///data')
        self.__DBSession = sessionmaker(bind=self.__engine)
        self.__session = self.__DBSession()

    def getSession(self):
        return self.__session
