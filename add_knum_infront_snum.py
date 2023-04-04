#adding last k numbers into front of list s with n numbers

n = int(input())
k = int(input())
s = []
s = input().split()[:n]
#print(s)
li1 =[]
if k==n:
    print(s)
elif k>0 and k<n:
    for i in range(len(s)-k,len(s)):
        li1.append(s[i])
    for i in range(0,len(s)-k):
        #print(i)
        li1.append(s[i])
for i in li1:
    print(i,end=" ")
#else:
 #   print('give valid number')


