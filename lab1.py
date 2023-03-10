import math
### Класс для дробей
class fractions:
    def proverka_two_minus(self, strochka):
        first, second = self.convert_nubers(strochka)
        first=str(first)
        second=str(second)
        if ("-" in first) and ("-" in second):
            first=first[1:len(first)]
            second=second[1:len(second)]
            res = str(first)+'/'+str(second)
            return res
        else:
            res = str(first)+'/'+str(second)
            return res
    def convert_nubers(self, res):
        index1 = res.find("/")
        first_chisl = int(res[0:index1] )
        first_zn =int(res[index1+1:len(res)])
        return first_chisl, first_zn
    def add_one(self, num: str):
        if '/' in num:
            return num
        else:
            num+="/1"
            return num
    def reduction(self, res):
        first_chisl, first_zn = self.convert_nubers(res)
        if(first_chisl%first_zn == 0):
            return str(int(first_chisl/first_zn))
        else:
            k = math.gcd(first_chisl, first_zn) 
            res = str(int(first_chisl//k))+'/'+str(int(first_zn//k))
            res=self.proverka_two_minus(res)
            return res
    def sum_num(self, a, b):
        a=self.add_one(a)
        b=self.add_one(b)
        first_chisl, first_zn = self.convert_nubers(a)
        second_chisl, second_zn = self.convert_nubers(b)
        res1=first_chisl*second_zn+ second_chisl*first_zn
        res2 = first_zn*second_zn
        res= str(res1)+'/'+str(res2)
        res = self.reduction(res)
        return res
    def subtraction(self, a, b):
        a=self.add_one(a)
        b=self.add_one(b)
        first_chisl, first_zn = self.convert_nubers(a)
        second_chisl, second_zn = self.convert_nubers(b)
        res1=first_chisl*second_zn - second_chisl*first_zn
        res2 = first_zn*second_zn
        res= str(res1)+'/'+str(res2)
        res = self.reduction(res)
        return res
    def multiplication(self, a, b):
        a=self.add_one(a)
        b=self.add_one(b)
        first_chisl, first_zn = self.convert_nubers(a)
        second_chisl, second_zn = self.convert_nubers(b)
        res1=first_chisl*second_chisl
        res2 = first_zn*second_zn
        res= str(res1)+'/'+str(res2)
        res = self.reduction(res)
        return res
    def division(self, a, b):
        a=self.add_one(a)
        b=self.add_one(b)
        first_chisl, first_zn = self.convert_nubers(a)
        second_chisl, second_zn = self.convert_nubers(b)
        res1=first_chisl*second_zn
        res2 = second_chisl*first_zn
        res= str(res1)+'/'+str(res2)
        res = self.reduction(res)
        return res
    def swap(self, el, row, column, matrix, column_work):
        max_el = self.add_one(matrix[el][column_work])
        i=el
        index= el
        first_chisl, first_zn = self.convert_nubers(max_el)
        max_el = float(first_chisl)/float(first_zn)
        for i in range(el+1, row):
            parametr = self.add_one(matrix[i][column_work])
            second_chisl, second_zn = self.convert_nubers(parametr)
            parametr = second_chisl/second_zn
            if parametr>max_el:
                max_el = parametr
                index = i

        matrix_help = matrix[index]
        matrix[index] = matrix[el] 
        matrix[el] = matrix_help
        return matrix
###########################

### Алгоритм гаусса собственно
def guse(matr, row, column, row_work):
    lab1 = fractions()
    column_work=0
    while(row_work<row):
        matrix = lab1.swap(row_work, row, column, matr,column_work)
        while(matr[row_work][column_work]=="0"):
            column_work+=1
            matrix = lab1.swap(row_work, row, column, matr,column_work)
            if column_work == column-1:
                return matr
            
        delen =matrix[row_work][column_work]
        for nums in range(row_work, column):
            matr[row_work][nums] = lab1.division(matr[row_work][nums],delen)
        # for el in matrix:
        #     print(el)
        for i in range(row_work+1, row):
            mnoj= matr[i][column_work]   
            for j in range(row_work, column):
                param = lab1.multiplication(mnoj, matr[row_work][j])
                matr[i][j] = lab1.subtraction(matr[i][j], param)
        for i in range(row_work-1,-1, -1):
            mnoj= matr[i][column_work]   
            for j in range(row_work, column):
                param = lab1.multiplication(mnoj, matr[row_work][j])
                matr[i][j] = lab1.subtraction(matr[i][j], param)
        # print()
        # for el in matrix:
        #     print(el)
        # print()
        row_work+=1
        column_work+=1
    return matr
def check_zeros(a):
    for i in range(len(a)-1):
        if a[i] != "0":
            return False
    return True 
def check_zeros_num(a):    
    if a != "0":
        return True
    else:
        return False    
### Функция для вывод ответа
def print_mas(matr, work_column,work_row, column, row):
    if work_row == row:
        return 0
    row_matr = matr[work_row]
    while check_zeros_num(row_matr[work_column])== False:
        work_column+=1
    res="X"+str(work_column+1)+" = "  
    res1="" 
    last_num = True
    if check_zeros_num(row_matr[-1]):
        res+=row_matr[-1]
        last_num = False
    work_column+=1
    while work_column< (column-2):
        if check_zeros_num(row_matr[work_column]):
            dop_num = prowerka_minus(row_matr[work_column])
            res1+=dop_num+"x"+str(work_column+1)
        work_column+=1
    if res1 =="" and last_num:
        res+=" 0"
    work_row+=1
    print(res+res1)
    print_mas(matr,0,work_row, column, row)

def prowerka_minus(num):
    if '-' in num:
        num=num[1:len(num)]
        num="+"+num
    else:
        num="-"+num
    return num
### заполнение массива
with open('matr.txt') as f:
    matrix = [list(map(str, row.split())) for row in f.readlines()]
######################
row = len(matrix)
column = len(matrix[0])
matrix = guse(matrix, row, column, 0)  
### Вывод ответа
help_m = matrix[-1]
if check_zeros(help_m) and help_m[column-1] != "0":
    print("No solutions!")
elif row!=(column-1):
    if check_zeros(help_m):
        print_mas(matrix,0,0, column,row-1)
    else:
        print_mas(matrix,0,0, column,row)
    print("Множество решений")
else:
    print_mas(matrix,0,0, column,row)
    print("Единственное решение")
################