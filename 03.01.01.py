import random

# создание 1 списка
matrix_1  = []
for i in range(10):
    a = random.randint(1,100), random.randint(1,100), random.randint(1,100),  random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)
    a = list(a)
    matrix_1.append(a)

print('matrix_1:')
for j in matrix_1:
    print(j) 

# создание 2 списка
matrix_2 = []
for i in range(10):
    a = random.randint(1,100), random.randint(1,100), random.randint(1,100),  random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)
    a = list(a)
    matrix_2.append(a)

#вывод в матрицу
print('   ')
print('matrix_2:')
for j in matrix_2:
    print(j) 
    
    
# сумма двух списхов
matrix_3 = []
for val, item in enumerate(matrix_1):
    newvals = []
    for itemval, insideitem in enumerate(item):
         newvals.append(insideitem + matrix_2[val][itemval])
         matrix_3.append(newvals)
         newvals = []
print('  ')
print('matrix_3:')
print(matrix_3)
