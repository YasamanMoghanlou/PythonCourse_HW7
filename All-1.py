#exercise
print ("1: ")
print ("yes")
print ("-------------")

#exercise 
print ("2: ")
print ("it will give you the numbers of the list from the end")
print ("-------------")

#exercise 
print ("3: ")
lst = [45, -3, 16, 8]
print (lst)
print ("-------------")

#exercise
print ("4: ")
lst = [10, -4, 11, 29]
print (lst[0])
print (lst[-1])

#what is lst[0] --> the first number = 10
#what is lst[3] --> the last number = 29
#what is lst[1] --> the second number = -4
#what is lst[-1] --> the first number from the end = 29
#what is lst[-4] --> the last number from the end = 10
# lst [3.0] is not legal

print ("-------------")
print ("5: ")

lst = [3, 0, 1, 5, 2]
x = 2 

print (lst[0])
print (lst[3])
print (lst[x])
print (lst[-x])
print (lst[x+1])
print (lst[x]+1)
print (lst[lst[x]])
print (lst[lst[lst[x]]])


print ("-------------")
print ("6 & 7: ")
print("the len() function")

print ("-------------")
print ("8: ")

lst = [20, 1, -34, 40, -8, 60, 1, 3]

print (lst) 

print (lst[0:3])

print (lst[4:8])

print (lst[4:33])

print (lst[-5:-3])

print (lst[-22:3])

print (lst[4:])

print (lst[:])

print (lst[:4])

print (lst[1:5])

print (-34 in lst)

print (-34 not in lst)

print (len(lst))

print ("-------------")
print ("9: ")
#347

lst = [2, 4, 6, 8, 10]

print (lst + [12, 14, 16, 18, 20])

print ("-------------")
print()
print ("10: ")
print ([8]*4)   #answer: [8, 8, 8, 8]

print()
print (6*[2, 7]) # answer: [2, 7, 2, 7, 2, 7, 2, 7, 2, 7, 2, 7]

print()
print ([1,2,3] + ['a', 'b', 'c', 'd']) #answer: [1, 2, 3, 'a', 'b', 'c', 'd']

print()
print (3*[1,2] + [4,2]) #answer: [1, 2, 1, 2, 1, 2, 4, 2]

print()
print (3*([1,2] + [4,2])) #answer: [1, 2, 4, 2, 1, 2, 4, 2, 1, 2, 4, 2]


print ("-------------")
print()
print ("11: ")
print([x+1 for x in [2,4,6,8]])  

print()
print([10*x for x in range (5,10)])

print()
print([x for x in range (10, 21) if x % 3 == 0])

print()
print([(x,y) for x in range (3) for y in range (4)])

print()
print([(x,y) for x in range (3) for y in range (4) if (x+y) % 2 ==0])


print ("-------------")
print()
print ("12: ")
print([x*x for x in [1, 2, 3, 4, 5]])

print()
print([x + 0.25 for x in [0, 0.25, 0.5, 0.75, 1.0, 1.25]])

print()
print([(x,y) for x in ('a' , 'b') for y in (0, 1, 2)])



print ("-------------")
print()
print ("13: ")
print('13. we can use a boolean expression to see the result')

print ("-------------")
print()
print ("14: ")
print('reverse will print the values from the end')

print ("-------------")
print()
print ("15: ")

def sum_positive(a):
    A = 0
    for num in a:
        if num > 0:
            A += num 
        else :
            pass
    return A

x = ([3, -3, 5, 2, -1, 2])

print(sum_positive(x))

print ("-------------")
print()
print ("16: ")
def count_even(list):
    if not list:
        return 0
    else:
        count = 0
        for i in range (len(list)):
            if list[i] % 2 == 0:
                count += 1
    return count

list = [3,5,4,-1,0]

    
print(list)
print(count_even(list))

print ("-------------")
print()
print ("17: ")

def print_big_enough(lst, num):
    for n in lst:
        if n >= num:
            
            print (n)
            
print_big_enough([2,4,6,8,1,3,5,7],4)


print ("-------------")
print()
print("18: ")

def next_number(list):
    number = 1
    if not list:
        return number
    for i in range(len(list)+1):
        if number in list:
            number += 1
        else:
            return number

n = int(input("How many numbers do you want to get?\n"))
list = []
for i in range (n):
    num = int(input())
    list.append(num)
    
print(list)
print(next_number(list))



print ("-------------")
print()
print("19: ")
def reverse (lst):
    return [ele for ele in reversed (lst)]
    
lst = [1, 2, 3, 4, 5]
print (reverse(lst))



print ("-------------")
print()
print("20: ")
m = [[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1]]

m[2][4] = 0


for row in m:         #process each row
    for elem in row:       #process each element in a given row
        print("{:4}" .format(elem), end="")
    print()
    
    
print ("-------------")
print()
print("21: ")
    
list1 = []
for i in range(1, 11):
    list1.append(i)
    
print(list1)

list2 = []
for i in range(1, 11):
    list2 += [i]
    
print(list2)

list3 = []
for i in range(10):
    list3.insert(i,i+1)
    
print(list3)

for i in range(10):
    list4 = [i+1 for i in range(10)]
    
print(list4)


list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
print(list5)

list6_1 = [1, 2, 3, 4, 5]
list6_2 = [6, 7, 8, 9, 10]
list6_1.extend(list6_2)
print(list6_1)

print ("-------------")
print()
print("22: ")



def x (matris, a, N):
	for i in range(N):
		for j in range(N):
			a[i][j] = matris[j][i]

def func (matris, N):
	
	a = [ [0 for j in range(len(matris[0])) ] for i in range(len(matris))]
	x (matris, a, N)
	for i in range(N):
		for j in range(N):
			if (matris[i][j] != a[i][j]):
				return False
	return True


matris = [ [ 1, 3, 5 ], [ 3, 2, 4 ], [ 5, 4, 1 ] ]
if (func(matris, 3)):
	print ("Yes")
else:
	print ("No")






