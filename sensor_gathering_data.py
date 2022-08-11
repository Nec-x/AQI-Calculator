import requests
import json
import math_functions as mf
import geocoding as gc
class Sensors:

    def __init__(self):
        self.og_call = None
        self.data = None
        self.file = None
        self.clat = None
        self.clon = None


    def add_file(self,file):
        self.file = file

    def add_coords(self,lat,lon):
        self.clat = lat
        self.clon = lon

    def get_sensor_data(self):
        '''This function will access the PurpleAir API, and retrieve information
            regarding all the sensors available on their site'''

        my_api_read_key = '1463D44A-0134-11ED-8561-42010A800005'
        my_url = 'https://api.purpleair.com/v1/sensors/?fields=pm2.5%2Clatitude%2Clongitude&location_type=0&max_age=3600'

        my_headers = {'X-API-Key': my_api_read_key}

        r = requests.get(my_url, headers=my_headers)

        return r

    def call_and_write_from_api(self, file = "previous_api_call.txt"):
        sensor_data = self.get_sensor_data()
        f = open(file, 'w')
        f.write(sensor_data.text)
        f.close()

    def collect_data(self, api = True):
        if api:
            data = self.get_sensor_data()
            self.og_call = data.json()
            #with open(self.file,'w') as jf:
            #    jf.write(json.dumps(data))
            self.data = self.og_call["data"]
        else:
            with open(self.file,'r') as jf:
                data = json.load(jf)
                self.data = data["data"]

    def sorted_sensor_list(self,sensor_data_list, miles, threshold):
        # Sorts sensors by the miles and threshold. Also sorts it by AQI
        new_list = []

        for sensor in sensor_data_list:
            if sensor[1] != None and sensor[2] != None and sensor[3] != None:
                aqi_lvl = mf.aq_level(sensor[3])
                distance = mf.latlon(self.clat,self.clon,sensor[1],sensor[2])
                if aqi_lvl >= threshold:
                    if distance <= miles:
                        new_list.append(sensor+[aqi_lvl])
        return sorted(new_list, key = lambda x: x[4], reverse = True)




'''
all = Sensors()

all.add_file('previous_api_call.txt')
all.add_coords(33.64283076, -117.841496)

all.collect_data(api = False)
info = all.sorted_sensor_list(all.data, 30, 30)
print(info)

aba = gc.Geocode()
aba.add_location("44341 Foxton Ave Lancaster, CA 93535")
print(aba.get_coords())
aba.add_sensors(info)
print('boo')
aba.get_locations(6)
'''