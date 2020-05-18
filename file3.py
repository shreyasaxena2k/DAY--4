dictionary= dict()
a=int(input('Enter the size of Dictionary: '))
for i in range(a):
    key=input('Enter the key for item'+str(i+1))
    value=int(input('Enter the value for item'+str(i+1)))
    dictionary[key]=value
val = list(dictionary.values())
val.sort()
print('THE SECOND LARGEST VALUE IN THE DICTIONARY IS : ',val[-2] )