import math
import copy
global d , tour_list,result_list
tour_list = []
result_list = []
d = 1000

def read_file():
    file_name = input('파일이름을 입력하시오 : ')
    with open(file_name,'r',encoding='UTF8') as f:
        global n, x_list, y_list , tour_list
        text = f.read()
        line = text.split('\n')
        n = int(line[0])  # 첫 줄의 첫 원소 = n
        x_list = []
        y_list = []
        for i in range(1,n+1):
            token = line[i].split()
            x_list.append(int(token[0]))
            y_list.append(int(token[1]))
        for i in range(0,n):
            tour_list.append(i)

def swap(k,i):
    global x_list,y_list,tour_list
    temp = x_list[k]
    x_list[k] = x_list[i]
    x_list[i] = temp
    temp = y_list[k]
    y_list[k] = y_list[i]
    y_list[i] = temp
    temp = tour_list[k]
    tour_list[k] = tour_list[i]
    tour_list[i] = temp

def tour(k):
    global n, x_list, y_list,d,tour_list,result_list
    if k==n:
        sum = 0
        result = 0
        for j in range(0,n-1):
            sum += (x_list[j]-x_list[j+1])**2
            sum += (y_list[j]-y_list[j+1])**2
            sum = sum**0.5
            result += sum
            sum=0
        result += (((x_list[n-1]-x_list[0])**2) + (y_list[n-1]-y_list[0])**2)**0.5
        if d > result:
            d = result
            result_list = copy.deepcopy(tour_list)
    for i in range(k, n):
        swap(k,i)
        tour(k+1)
        swap(k,i)
read_file()
tour(1)
print(d,'\n',result_list)
