#使用list和tuple
a = ['A', 'B', 'C']
print(a[1])
print(a[-1])
a.append('D')
print(a[3])

a.insert(0,'0')
print(a[0])

a.insert(1,'a')
print(a[1])

a.pop()
print(a)

a.pop(0)
print(a)

a[0] = 'AA'
print(a)

a[2] = 3
print(a)

a[0] = 123,'123'
print(a)
print(len(a))

b = (1,)
print(b)
b = (1,2,[3,4])
print(b)
b[2][1] = 5
print(b)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0], L[1][1], L[2][2])
