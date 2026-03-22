
import numpy as np

#1
print('ex1')
arr = np.arange(10)
print(arr)

#2
print('ex2')
lst = [3.14, 2.17, 0, 1, 2]

arr = np.array(lst, dtype=int)
print(arr)

#3
print('ex3')
arr = np.arange(1, 10).reshape(3, 3)
print(arr)

#4
print('ex4')
arr = np.random.rand(4, 5)
print(arr)

#5
print('ex5')
arr = np.array([
    [21,22,23,22,22],
    [20,21,22,23,24],
    [21,22,23,22,22]
])

second_row = arr[1]
print(second_row)

#6
print('ex6')
arr = np.arange(10)

reversed_arr = arr[::-1]
print(reversed_arr)

#7
print('ex7')
identity = np.eye(4)
print(identity)

#8
print('ex8')
arr = np.arange(10)

total = np.sum(arr)
average = np.mean(arr)

print("Sum:", total, "Average:", average)

#9
print('ex9')
arr = np.arange(1, 21).reshape(4, 5)
print(arr)

#10
print('ex10')
arr = np.arange(10)

odd_numbers = arr[arr % 2 != 0]
print(odd_numbers)