import math
import time

R = 6371000.0 # радиус планеты в метрах

start_lat = 59.0 # Широта
start_lon = 49.0 # Долгота
start_angle = 0 # стартовый угол
machine_dist = 500 # длина стрелы

# преобразование углов в радианы
def to_radians(angle):
    return angle * math.pi / 180

# преобразование радиан в углы
def to_angle(radians):
    return radians * 180 / math.pi

# расчет дальней точки поливной установки
def calc_endpoint(Lat, Lon, bearingAngle, distance):
    phi1 = to_radians(Lat)
    lambda1 = to_radians(Lon)
    deltaDistance = distance / R
    theta = to_radians(bearingAngle)
    sinPhi2 = math.sin(phi1) * math.cos(deltaDistance) + math.cos(phi1) * math.sin(deltaDistance) * math.cos(theta)
    phi2 = math.asin(sinPhi2)

    x = math.cos(deltaDistance) - math.sin(phi1) * sinPhi2
    y = math.sin(theta) * math.sin(deltaDistance) * math.cos(phi1)

    lambda2 = lambda1 + math.atan2(y, x)
    lat2 = to_angle(phi2)
    lon2 = to_angle(lambda2)
            
    return (lat2, lon2)

# нормализация угла (обработка отрицательных значений)
def normalize_angle(bearingAngle):
    return bearingAngle if bearingAngle >= 0  else bearingAngle + 360
    
while True:
    result = calc_endpoint(start_lat, start_lon, start_angle, machine_dist)
    print(result)
    time.sleep(5)
    start_angle+=1