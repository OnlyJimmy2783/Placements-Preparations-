arr = [4,1,7,3]

first = float('-inf')
second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print(second)
'''

for : 4

num = 4

for 4 in arr:
    if 4 > first: # 4 > -inf
        second = first # second = -inf
        first = 4 # first = 4

-----------------------------------------------------
for : 1

num = 1

for 1 in arr:
    if 1 > 4:   # 1 > 4 is False
        elif 1 > '-inf' and 1! = 4:
            second = 1


'''