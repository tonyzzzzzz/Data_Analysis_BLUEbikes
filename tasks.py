#!/usr/bin/python
# coding:utf-8
# Data Analysis

import sqlalchemy

import statistics
from models.tripdata import tripdata
from models.station import station
from tools.database import Database

session = Database().getSession()


def q1():
    bikeids = session.query(tripdata.bikeid).all()
    count = {}
    for bikeid in bikeids:
        if bikeid[0] in count:
            count[bikeid[0]] += 1
        else:
            count[bikeid[0]] = 1
    print('All Used Bikes Count: ' + str(len(count)))


def q2():
    station_name = session.query(station).filter(station.id == 189).first().station_name
    print('\nStation Name: ' + station_name)

    trips_originate_at_189 = session.query(tripdata).filter(tripdata.start_station_id == 189).all()
    print('Trips Originate At 189: ' + str(len(trips_originate_at_189)))

    trips_end_at_189 = session.query(tripdata).filter(tripdata.end_station_id == 189).all()
    print('Trips End At 189: ' + str(len(trips_end_at_189)))


def q3():
    formatted_durations = list(a[0] for a in session.query(tripdata.tripduration).all())
    print('\nMean Trip Duration: ' + str(statistics.mean(formatted_durations)))
    print('Median Trip Duration: ' + str(statistics.median(formatted_durations)))


def main():
    q1()
    q2()
    q3()


if __name__ == '__main__':
    main()

