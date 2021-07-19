s = 'apple'
temp = []

for sti in s:
    i = 0
    for stj in s:
        if stj in sti:
            # temp.append(stj)
            i += 1


a = [1, 2]
b = [3, 4]
Output: [1, 2, 3, 4]

c = a+b
c = a.extend(b)

a = [[1, 2]]
b = [[3, 4]]

Output: [1, 2, 3, 4]
# output: [[1, 2], [3,4]]


