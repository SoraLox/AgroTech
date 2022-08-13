import math
import time

R = 6371000.0  # радиус планеты в метрах

start_lat = 59.0  # Широта
start_lon = 49.0  # Долгота
start_angle = 0  # стартовый угол
machine_dist = 500  # длина стрелы

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
    sinPhi2 = math.sin(phi1) * math.cos(deltaDistance) + \
        math.cos(phi1) * math.sin(deltaDistance) * math.cos(theta)
    phi2 = math.asin(sinPhi2)

    x = math.cos(deltaDistance) - math.sin(phi1) * sinPhi2
    y = math.sin(theta) * math.sin(deltaDistance) * math.cos(phi1)

    lambda2 = lambda1 + math.atan2(y, x)
    lat2 = to_angle(phi2)
    lon2 = to_angle(lambda2)

    return (lat2, lon2)

# нормализация угла (обработка отрицательных значений)


def normalize_angle(bearingAngle):
    return bearingAngle if bearingAngle >= 0 else bearingAngle + 360


result = calc_endpoint(start_lat, start_lon, start_angle, machine_dist)

result_formated = str(result).replace("(", " ")
result_formated1 = str(result).replace(")", " ")
result_formated2 = str(result).replace(",", " ")

result_splitted = result_formated2.split()

latT = str(result_splitted[0])
latTT = latT.replace("(", "")
lonT = str(result_splitted[1])
lonTT = lonT.replace(")", "")
print(latTT, "\n", lonTT)

f1 = open('work/lat.txt', 'w')
f1.write(str(latTT))
f1.close()

f2 = open('work/lon.txt', 'w')
f2.write(str(lonTT))
f2.close()

print(result_splitted)

time.sleep(5)
start_angle += 1
