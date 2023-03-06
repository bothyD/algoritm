import math
from lab1 import *  
### Функция для вывод ответа
def print_massiv(mas):
    for el in mas:
        print(el)
    print()
def find_basis(matr):
    for i in range(0, row):
        for j in range(0, row):
            column_new=stroka[j]
            matr[i][j]=matrix[i][column_new]
            matr[i][row]=matrix[i][column-1]
    return
def proveraka_basisa(massive, matr_basis_str):
    for i in range(0, len(massive)):
        if(massive[i][0]==massive[i][1] and massive[-1]!=0):
            print("Линейно зависимы: ")
            print_massiv(massive) 
            return
    print_massiv(massive) 
    print_mas(massive,0,0, row+1,row)
    for i in range(row):
        matr_basis[matr_basis_str][stroka[i]]=new_matr[i][row]

    matr_basis_str+=1
def print_mas(matr, work_column,work_row, column, row):
    if work_row == row:
        return 0
    row_matr = matr[work_row]
    res1=""    
    while work_column< (column-1):
        if check_zeros_num(row_matr[work_column]):
            dop_num = prowerka_minus(row_matr[work_column])
            res1+=dop_num+"x"+str(work_column+1)
        work_column+=1
    
    res1+=" = "+ row_matr[-1]
    #if res1[0]=="+":
    res1=res1[1:len(res1)]
    work_row+=1
    print(res1)
    print_mas(matr,0,work_row, column, row)

def prowerka_minus(num):
    if '-' in num:
        num=num[1:len(num)]
        num="-"+num
    else:
        num="+"+num
    return num
def comb(n, k):
    """Генерация сочетаний из `n` по `k` без повторений."""
    d = list(range(0, k))
    yield d
    while True:
        i = k - 1
        while i >= 0 and d[i] + k - i + 1 > n:
            i -= 1
        if i < 0:
            return
        d[i] += 1
        for j in range(i + 1, k):
            d[j] = d[j - 1] + 1
        yield d

### заполнение массива
with open('matrix.txt') as f:
    matrix = [list(map(str, row.split())) for row in f.readlines()]
print_massiv(matrix)
######################
row = len(matrix)
column = len(matrix[0])
guse(matrix, row, column, 0)  
print_massiv(matrix)
### Вывод ответа
help_m = matrix[-1]
if check_zeros(help_m) and help_m[column-1] != "0":
    print("No solutions!")
elif row!=(column-1):
    print("Общее решение:")
    if check_zeros(help_m):
        del(matrix[-1])
        row-=1
        print_mas(matrix,0,0, column,row)
    else:
        print_mas(matrix,0,0, column,row)
    c=math.factorial(column-1)/ (math.factorial(row) *  math.factorial(column-1-row))
    print("Кол-во базисных решений: ", int(c))
    new_matr = [[str(0) for j in range(0,row+1)] for i in range(0,row)]
    matr_basis = [[str(0) for j in range(0,column-1)] for i in range(0,int(c))]
    matr_basis_str=0
    print("\n Базисные решения: ")
    for stroka in comb(column-1, row): 
            print("##############################")      
            print("\t",stroka,"\t")
            find_basis(new_matr)        
            print_massiv(new_matr)      
            new_matr =guse(new_matr, row, row+1, 0)
            print_massiv(new_matr)
            #print_mas(new_matr,0,0, row+1,row)
            #proveraka_basisa(new_matr,matr_basis_str)
            
    # print("\n Базисные решения: ")
    # new_i=len(matr_basis[0])
    # for el in range(0, len(matr_basis)):
    #     for el_i in range(0,new_i):
    #         print("x",el_i+1," = ", matr_basis[el][el_i])
    #     print()

    
else:
    print_mas(matrix,0,0, column,row)
    print("Единственное решение")
################
