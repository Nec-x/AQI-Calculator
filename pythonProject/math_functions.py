import math

def aqi(x1 = 0,x2 = 0,y1 = 0,y2 = 0,mpu = 0):
    eq = y1 + (mpu - x1) * ((y2 - y1) / (x2 - x1))
    return rounder(eq)


def rounder(num) -> int:
    '''Rounds the number cause round() is weird.'''

    sting = str(num)
    if '.5' in sting:
        return math.ceil(num)
    else:
        return round(num)


def aq_level(mp) -> int:
    '''This translates the mp^3 level to air quality level'''

    if 0 <= mp < 12.1:
        return aqi(x2 = 12.0, y2 = 50,mpu = mp)
    elif 12.1 <= mp < 35.5:
        return aqi(x1 = 12.1,x2 = 35.4,y1 = 51,y2 = 100,mpu = mp)
    elif 35.5 <= mp < 55.5:
        return aqi(x1 = 35.5,x2 = 55.4,y1 = 101,y2 = 150,mpu = mp)
    elif 55.5 <= mp < 150.5:
        return aqi(x1 = 55.5,x2 = 150.4,y1 = 151,y2 = 200,mpu = mp)
    elif 150.5 <= mp < 250.5:
        return aqi(x1 = 150.5,x2 = 250.4,y1 = 201,y2 = 300,mpu = mp)
    elif 250.5 <= mp < 350.5:
        return aqi(x1 = 250.5,x2 = 350.4,y1 = 301,y2 = 400,mpu = mp)
    elif 350.5 <= mp < 500.5:
        return aqi(x1 = 350.5,x2 = 500.4,y1 = 401,y2 = 500,mpu = mp)
    elif mp >= 500.5:
        return 501


def latlon(clat1, clon1, lat2, lon2):
    clat1 = clat1 * (math.pi / 180)
    lat2 = lat2 * (math.pi / 180)
    clon1 = clon1 * (math.pi / 180)
    lon2 = lon2 * (math.pi / 180)

    dlat = clat1 - lat2
    dlon = clon1 - lon2
    alat = (clat1 + lat2) / 2
    R = 3958.8
    x = dlon * math.cos(alat)
    d = math.sqrt(x ** 2 + dlat ** 2) * R
    return d


