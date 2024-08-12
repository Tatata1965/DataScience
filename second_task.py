
import math
def cosine_distance(v1,v2):

    sumx, sumxy, sumy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumx += x*x
        sumy += y*y
        sumxy += x*y
        if x == 0 and y == 0:
            print('векторы состоят только из нулей, валидация не пройдена')
        elif len(v1)!= len(v2):
            print('длины списков не совпадают, валидация не пройдена')
        else:
            cosDist = sumxy/math.sqrt(sumx*sumy)
    return print(f"Косинусное расстояние векторов {v1} и {v2} равно {cosDist}")



cosine_distance([5,7,9,22,44], [2, 54, 66, 55, 999])

