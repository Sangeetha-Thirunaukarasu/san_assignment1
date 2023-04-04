#find the maxximum number in the given string
# using string comprehension
s = input()
#print(s)
l = [i.strip('.') for i in s.split()]
#print(l)
res = [int(i) for i in l if i.isnumeric()]
#print(res)
print(max(res))