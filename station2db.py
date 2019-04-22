#!/usr/bin/python
# coding:utf-8
# Convert Raw Station Data to SQLLite

import sqlalchemy
import csv
import json
from models.tripdata import tripdata
from tools.database import Database
from models.station import station


def main():
    f = open('rawdata.csv', 'r')
    reader = csv.DictReader(f)
    trips = []
    stations = {}
    for line in reader:
        trips.append(line)
    for trip in trips:
        stations[int(trip['start station id'])] = {
            'station_name': trip['start station name'],
            'latitude': trip['start station latitude'],
            'longitude': trip['start station longitude']
        }
        stations[int(trip['end station id'])] = {
            'station_name': trip['end station name'],
            'latitude': trip['end station latitude'],
            'longitude': trip['end station longitude']
        }
    sorted_stations = (sorted(stations.items(), key=lambda item: item[0]))

    session = Database().getSession()
    for a in sorted_stations:
        nStation = station(
            id=a[0],
            station_name=a[1]['station_name'],
            latitude=a[1]['latitude'],
            longitude=a[1]['longitude']
        )
        session.add(nStation)
    session.commit()
    session.close()


if __name__ == '__main__':
    main()

