a=dict()
b=dict()
size=int(input('Enter the size: '))
for i in range (size):
    key = input('Enter the key for item' + str(i + 1))
    value = int(input('Enter the value for item' + str(i + 1)))
    a[key] = value
for key,value in a.items():
    if value not in b.values():
        b[key]=value
print('NEW DICTIONARY IS : ',b)
