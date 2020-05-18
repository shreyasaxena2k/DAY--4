n=int(input('ENter the number of votes: '))
a=[]
for i in range(n):
    a.append(input('Enter the name of candidate: '))
b=[]
for name in a:
    b.append((name, a.count(name)))
b.sort(key=lambda x:x[0],reverse=True)
b.sort(key=lambda x:x[1])
print('won', b[-1][0])