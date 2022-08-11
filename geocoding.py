import json
import urllib.request
from pathlib import Path
import math_functions as mf

class Geocode:
    def __init__(self):
        self.sensors = None
        self.location = None

    def add_location(self, location):
        self.location = location

    def add_sensors(self, sensors):
        self.sensors = sensors

    def get_coords(self):
        linked = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode([('q', self.location), ('format', 'json')])

        request = urllib.request.Request(linked, headers={
            'Referer': 'https://www.ics.uci.edu/~thornton/ics32/ProjectGuide/Project3/#####'})
        response = urllib.request.urlopen(request)
        text = json.loads(response.read().decode("utf-8"))
        response.close()
        if text == []:
            return None
        else:
            for i in text:
                dic = i
            lat = float(dic['lat'])
            lon = float(dic['lon'])
            return lat, lon

    def get_locations(self,max):
        newl = []
        for sensor in self.sensors:
            print()
            if max == 0:
                return newl

            linked = f'https://nominatim.openstreetmap.org/reverse?' + urllib.parse.urlencode([('lat', sensor[1]), ('lon', sensor[2]), ('format', 'json')])

            request = urllib.request.Request(linked, headers={
                'Referer': 'https://www.ics.uci.edu/~thornton/ics32/ProjectGuide/Project3/#####'})
            response = urllib.request.urlopen(request)

            data = response.read()

            text = json.loads(data.decode("utf-8"))

            response.close()
            newl.append([sensor[1],sensor[2],sensor[4],text['display_name']])

            max -= 1
        return newl