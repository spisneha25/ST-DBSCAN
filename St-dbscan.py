import math
from xlrd import *
Noise = 999999
Unmarked = 99999
filename = input('Enter file location:')
book = open_workbook(filename)
csheet = book.sheet_by_index(0)
rw = csheet.nrows
#rw = 30
D = {}
C = {}
X = {}
T = {}
K = {}
Cluster_Label = 0
Minpts = math.log(rw)
#print(Minpts)
count = 0
stack = 0

print(Minpts)

def eps1(x, y):
    return math.sqrt((x.lat - y.lat)**2 + (x.lon - y.lon)**2)

def eps2(x, y):
    return math.sqrt((x.y1 - y.y1)**2 + (x.y2 - y.y2)**2)

def Retrieve_Neighbours(x, n):
    T = {}
    Y = {}
    count = 0
    for r in range(rw):
        if n == r:
            continue
        else:
            e1 = eps1(x, D[r])
            e2 = eps2(x, D[r])
            print(e1, e2)
            if(e1 < 0.8 and e2 < 0.4):
                Y[count] = Data(D[r].acode, D[r].lat, D[r].lon,  D[r].y1, D[r].y2, D[r].value)
                T[count] = r
                count += 1
               # print(count)
    return Y
    

def push(x):
     Y = {}
     for j in range(count):
         Y[stack] = Data(D[T[j]].acode, D[T[j]].lat, D[T[j]].lon,  D[T[j]].y1, D[T[j]].y2, D[T[j]].value)
         K[stack] = T[j]
         stack = stack + 1

def pop():
    stack = stack - 1
    return Y[stack]

class Data:
    acode = 0.0
    lat = 0.0
    lon = 0.0
    y1 = 0.0
    y2 = 0.0
    value = 0.0
    clabel = Unmarked
    def __init__(self, acode, lat, lon, y1, y2, value):
        self.lat = lat
        self.lon = lon
        self.y1 = y1
        self.y2 = y2
        self.acode = acode
        self.value = value
        
for r in range(rw):
    r0 = float(csheet.cell(r,0).value)
    r1 = float(csheet.cell(r,3).value)
    r2 = float(csheet.cell(r,4).value)
    r3 = float(csheet.cell(r,1).value)
    r4 = float(csheet.cell(r,2).value)
    r5 = float(csheet.cell(r,5).value)
    D[r] = Data(r0, r1, r2, r3, r4, r5)
    
for r in range(rw):
    if D[r].clabel == Unmarked:
        X = Retrieve_Neighbours(D[r], r)
        if count < Minpts:
            D[r].clabel = Noise
        else :
            Cluster_label = Cluster_label + 1
            for j in range(count):
                D[T[j]].clabel = Cluster_label
                #print(D[T[j]].acode, D[T[j]].clabel)
                push(D[T[j]])

                while(stack < 0):
                    CurrentObj = pop()
                    X = Retrieve_Neighbors(CurrentObj, K[stack])

                    if count < Minpts:
                        for j in range(count):
                            if D[T[j]].clabel != Noise or D[T[j]].clabel == Unmarked:
                                D[T[j]].clabel = Cluster_label
                                Push(D[T[j]])
                    
                

            
                




                



    
