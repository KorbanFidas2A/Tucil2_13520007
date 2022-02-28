from functools import update_wrapper
from re import M
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from numpy.linalg import norm

import sys
sys.setrecursionlimit(15000)


class Point:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx

#memberikan nomor urut terhadap data yang telah diambil dari dataset Iris
def give_nomor_urut(bucket):
    point_dict = []
    for i in range (len(bucket)):
        p1 = Point(bucket[i][0], bucket[i][1], i)
        point_dict.append(p1)
    return point_dict

#mengambil area konveks sesuai dengan urutan P1-P2 (sehingga penggunaannya tinggal dibalik, jika ingin arah yang berlawanan P2-P1)
#mencari daerah S1 / S2
def area_convex(P1, P2, point_dict):
    area = []
    for i in range (len(point_dict)):
        if(point_dict[i] != P1 and point_dict[i] != P2):
            P3 = point_dict[i]
            det = P1.x*P2.y + P3.x*P1.y + P2.x*P3.y - P3.x*P2.y - P2.x*P1.y - P1.x*P3.y
            if(det <= 0):
                area.append(P3)
    return area


#mencari titik paling jauh setelah mendapatkan kumpulan titik2
def far_point(P1, P2, area):
    array1 =np.array([P1.x, P1.y])
    array2 = np.array([P2.x, P2.y])
    array3 = np.array([area[0].x, area[0].y])
    max = (np.abs(np.cross(array2-array1, array1-array3)) / norm(array2-array1))
    point = area[0]
    for i in range (1, len(area)):
        array3 = np.array([area[i].x, area[i].y])
        length = (np.abs(np.cross(array2-array1, array1-array3)) / norm(array2-array1))
        if(max < length):
            max = length
            point = area[i]
    return point


#mencari titik-titik hull yang dikelompokkan menjadi 1 array
def findHull(area, P1, P2, point_dict):
    if(len(area) == 0):
        return [[P1.idx, P2.idx]]
    elif(len(area) == 1):
        return [[P1.idx, area[0].idx], [area[0].idx, P2.idx]]
    else:
        solution = []
        far = far_point(P1, P2, area)
        area_below = area_convex(P1, far, point_dict)
        area_upper = area_convex(far, P2, point_dict)
        below_hull = findHull(area_below, P1, far, point_dict)
        upper_hull = findHull(area_upper, far, P2, point_dict)
        
        #tambahkan
        for i in below_hull:
            solution.append(i)
        for i in upper_hull:
            solution.append(i)
        return solution
    

def myConvexHull(bucket):
    point_dict = give_nomor_urut(bucket)
    full_solution = []
    #minimum point
    P1 = point_dict[0]
    #maximum point
    P2 = point_dict[0]
    for i in range (1, len(point_dict)):
        current_point = Point(point_dict[i].x, point_dict[i].y, point_dict[i].idx)
        if(P1.x > current_point.x):
            P1 = current_point
        if(P2.x < current_point.x):
            P2 = current_point

    #atas / kiri
    left_area = area_convex(P2, P1, point_dict)
    
    #bawah / kanan
    right_area = area_convex(P1, P2, point_dict)
    

    #mencari daerah kiri/atas
    upper_solution = findHull(left_area, P2, P1, point_dict)

    #mencari daerah kanan/bawah
    bottom_solution = findHull(right_area, P1, P2, point_dict) 


    full_solution = []
    for i in range (len(upper_solution) + len(bottom_solution)):
        if(i < len(upper_solution)):
            full_solution.append(upper_solution[i])
        elif(i >= len(upper_solution)):
            full_solution.append(bottom_solution[i-len(upper_solution)])

    return full_solution
